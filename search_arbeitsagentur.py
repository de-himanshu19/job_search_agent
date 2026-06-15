import requests
import base64
import json
import time
import pandas as pd

from config import TARGET_ROLES, NEGATIVE_KEYWORDS
from job_scorer import calculate_score
from telegram_sender import send_telegram_message
from job_history import filter_new_jobs, mark_jobs_as_sent
from search_company_careers import format_company_career_message

BASE_URL = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/jobs"

HEADERS = {
    "X-API-Key": "jobboerse-jobsuche"
}


def get_city(job):
    locations = job.get("stellenlokationen", [])
    if locations and isinstance(locations, list):
        address = locations[0].get("adresse", {})
        return address.get("ort", "")
    return ""


def get_job_link(job):
    external_url = job.get("externeURL")
    if external_url:
        return external_url

    ref = job.get("referenznummer", "")
    if ref:
        return f"https://www.arbeitsagentur.de/jobsuche/jobdetail/{ref}"

    return ""


def search_jobs_for_role(role, location="Deutschland", size=25):
    params = {
    "was": role,
    "wo": location,
    "angebotsart": "1",
    "size": size,
    "page": 1,
    "veroeffentlichtseit": 7
}

    response = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=20)

    if response.status_code != 200:
        print(f"Error for role: {role}")
        print("Status code:", response.status_code)
        print(response.text[:500])
        return []

    data = response.json()

    # Correct key from Arbeitsagentur API
    jobs = data.get("ergebnisliste", [])

    results = []

    for job in jobs:
        title = job.get("stellenangebotsTitel", "")
        company = job.get("firma", "")
        city = get_city(job)
        ref = job.get("referenznummer", "")
        published = job.get("datumErsteVeroeffentlichung", "")
        profession = job.get("hauptberuf", "")
        link = get_job_link(job)

        results.append({
            "source": "Arbeitsagentur",
            "search_role": role,
            "title": title,
            "company": company,
            "city": city,
            "published": published,
            "profession": profession,
            "ref": ref,
            "link": link
        })

    return results


def remove_bad_jobs(jobs):
    clean_jobs = []

    for job in jobs:
        combined_text = f"{job['title']} {job['company']} {job['profession']}".lower()

        is_bad = False

        for negative in NEGATIVE_KEYWORDS:
            if negative.lower() in combined_text:
                is_bad = True
                break

        if not is_bad:
            clean_jobs.append(job)

    return clean_jobs

DETAIL_BASE_URL = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobdetails"


GERMAN_LANGUAGE_BLOCKERS = [
    # Very high German level
    "verhandlungssichere deutschkenntnisse",
    "verhandlungssicheres deutsch",
    "verhandlungssicher in deutsch",
    "deutsch verhandlungssicher",
    "deutschkenntnisse verhandlungssicher",
    "sehr gute deutschkenntnisse",
    "sehr gutes deutsch",
    "fließende deutschkenntnisse",
    "fliessende deutschkenntnisse",
    "fließend deutsch",
    "fliessend deutsch",
    "deutsch fließend",
    "deutsch fliessend",
    "deutschkenntnisse auf muttersprachlichem niveau",
    "muttersprachliche deutschkenntnisse",
    "deutsch auf muttersprachlichem niveau",

    # Formal levels
    "deutsch c1",
    "deutsch c2",
    "c1 deutsch",
    "c2 deutsch",
    "german c1",
    "german c2",
    "fluent german",
    "native german",

    # Strong German requirement phrases
    "ausgezeichnete deutschkenntnisse",
    "hervorragende deutschkenntnisse",
    "perfekte deutschkenntnisse",
    "deutschkenntnisse in wort und schrift auf sehr gutem niveau",
    "sehr gute kenntnisse der deutschen sprache"
]
ENGLISH_SIGNAL_KEYWORDS = [
    "english",
    "englisch",
    "gute englischkenntnisse",
    "sehr gute englischkenntnisse",
    "very good english",
    "fluent english",
    "international",
    "internationales team",
    "global",
    "multinational"
]

GERMAN_RISK_KEYWORDS = [
    "kundenberatung",
    "telefonische kundenbetreuung",
    "privatkunden",
    "privatkundenberatung",
    "firmenkundenberatung",
    "firmenkunden",
    "filialgeschäft",
    "filiale",
    "sachbearbeiter",
    "sachbearbeitung",
    "kundenservice",
    "kundenbetreuung",
    "beratungsgespräche",
    "schriftliche und telefonische kommunikation",
    "direkter kundenkontakt",
    "persönliche kundenberatung",
    "telefonisch",
    "telefonische kommunikation",
    "korrespondenz mit kunden",
    "ansprechpartner für kunden",
    "betreuung unserer kunden",
    "serviceorientiert",
    "kundenanfragen",
    "deutschsprachigen kunden"
]

def encode_ref_number(ref):
    encoded = base64.urlsafe_b64encode(ref.encode("utf-8")).decode("utf-8")
    return encoded.rstrip("=")


def fetch_job_details(ref):
    if not ref:
        return ""

    encoded_ref = encode_ref_number(ref)
    url = f"{DETAIL_BASE_URL}/{encoded_ref}"

    response = requests.get(url, headers=HEADERS, timeout=20)

    if response.status_code != 200:
        return ""

    data = response.json()

    # Convert full JSON to searchable text
    detail_text = json.dumps(data, ensure_ascii=False).lower()

    return detail_text


def is_german_fluent_required(detail_text):
    if not detail_text:
        return False

    for blocker in GERMAN_LANGUAGE_BLOCKERS:
        if blocker in detail_text:
            return True

    return False

def has_english_signal(detail_text):
    if not detail_text:
        return False

    for keyword in ENGLISH_SIGNAL_KEYWORDS:
        if keyword in detail_text:
            return True

    return False


def has_german_risk_signal(detail_text):
    if not detail_text:
        return False

    for keyword in GERMAN_RISK_KEYWORDS:
        if keyword in detail_text:
            return True

    return False

def filter_german_fluent_jobs(df):
    filtered_rows = []

    for _, row in df.iterrows():
        ref = row.get("ref", "")

        detail_text = fetch_job_details(ref)

        time.sleep(0.2)

        if is_german_fluent_required(detail_text):
            print(f"Removed due to fluent German requirement: {row['title']} - {row['company']}")
            continue

        row = row.copy()
        row["english_signal"] = has_english_signal(detail_text)
        row["german_risk_signal"] = has_german_risk_signal(detail_text)

        filtered_rows.append(row)

    return pd.DataFrame(filtered_rows)

def print_job_age_summary(df, label):
    if df.empty or "published" not in df.columns:
        print(f"{label}: No jobs to analyze.")
        return

    temp_df = df.copy()
    temp_df["published_date"] = pd.to_datetime(temp_df["published"], errors="coerce")

    valid_dates = temp_df.dropna(subset=["published_date"])

    if valid_dates.empty:
        print(f"{label}: No valid published dates found.")
        return

    newest = valid_dates["published_date"].max()
    oldest = valid_dates["published_date"].min()

    today = pd.Timestamp.today().normalize()

    valid_dates["days_old"] = (today - valid_dates["published_date"]).dt.days

    print(f"\n{label}")
    print(f"Newest job date: {newest.date()}")
    print(f"Oldest job date: {oldest.date()}")
    print(f"Newest job age: {valid_dates['days_old'].min()} days")
    print(f"Oldest job age: {valid_dates['days_old'].max()} days")

def print_signal_summary(df):
    if df.empty:
        print("No signal summary available.")
        return

    english_count = 0
    german_risk_count = 0

    if "english_signal" in df.columns:
        english_count = df["english_signal"].sum()

    if "german_risk_signal" in df.columns:
        german_risk_count = df["german_risk_signal"].sum()

    print("\nSignal summary:")
    print(f"Jobs with English-friendly signal: {english_count}")
    print(f"Jobs with German-heavy risk signal: {german_risk_count}")

def main():
    all_jobs = []

    for role in TARGET_ROLES:
        print(f"Searching: {role}")
        jobs = search_jobs_for_role(role, location="Deutschland", size=10)
        all_jobs.extend(jobs)

    print("\nSearch summary:")
    print(f"Total jobs collected before cleaning: {len(all_jobs)}")

    clean_jobs = remove_bad_jobs(all_jobs)
    print(f"Jobs after basic negative keyword filter: {len(clean_jobs)}")

    df = pd.DataFrame(clean_jobs)

    if df.empty:
        print("No jobs found.")
        return

    before_duplicates = len(df)
    df = df.drop_duplicates(subset=["ref"])
    print(f"Duplicate jobs removed: {before_duplicates - len(df)}")
    print(f"Jobs after duplicate removal: {len(df)}")

    print_job_age_summary(df, "Job age before German language filtering")
    

    print("\nChecking job details for German language requirements...")
    before_language_filter = len(df)

    df = filter_german_fluent_jobs(df)

    after_language_filter = len(df)

    print("\nLanguage filter summary:")
    print(f"Jobs before German language filter: {before_language_filter}")
    print(f"Jobs removed due to fluent/business German requirement: {before_language_filter - after_language_filter}")
    print(f"Jobs after German language filter: {after_language_filter}")

    if df.empty:
        print("No jobs left after German language filtering.")
        return

    print_job_age_summary(df, "Job age after German language filtering")
    print_signal_summary(df)

    df[["score", "reasons"]] = df.apply(
        lambda row: pd.Series(calculate_score(row.to_dict())),
        axis=1
    )

    df = df.sort_values(by="score", ascending=False)

    print("\nChecking already-sent jobs...")
    before_history_filter = len(df)

    new_jobs_df = filter_new_jobs(df)

    print(f"Jobs before history filter: {before_history_filter}")
    print(f"Jobs already sent before: {before_history_filter - len(new_jobs_df)}")
    print(f"New jobs available today: {len(new_jobs_df)}")

    if new_jobs_df.empty:
        message = (
            "Good morning USER!\n\n"
            "No new banking/data analyst jobs found today.\n\n"
            f"Jobs checked after filters: {before_history_filter}\n"
            "I will check again tomorrow."
        )
        send_telegram_message(message)
        print("No new jobs to send.")
        return

    top_jobs = new_jobs_df.head(10)

    message = (
    "Good morning USER!\n\n"
    "Here are your top banking/data analyst jobs today.\n\n"
    "Search summary:\n"
    f"Collected jobs: {len(all_jobs)}\n"
    f"After duplicate removal: {before_language_filter}\n"
    f"After German filter: {after_language_filter}\n"
    f"New jobs available: {len(new_jobs_df)}\n"
    "Job age: 0–7 days\n\n"
    "Top jobs:\n\n"
    )

    for number, (_, row) in enumerate(top_jobs.iterrows(), start=1):
        message += (
            f"{number}. {row['title']}\n"
            f"{row['company']} | {row['city']}\n"
            f"Score: {row['score']}/100\n"
            f"{row['link']}\n\n"
        )

    jobs_sent = send_telegram_message(message)

    # company_message = format_company_career_message(limit=6)
    # company_sent = send_telegram_message(company_message)

    if jobs_sent:
        mark_jobs_as_sent(top_jobs)
        print("Top jobs marked as sent.")
    else:
        print("Jobs were NOT marked as sent because Telegram sending failed.")

    # if not company_sent:
    #     print("Company career message was not sent.")

    print("\nTop matched jobs:")
    print(df[[
        "score",
        "title",
        "company",
        "city",
        "published",
        "profession",
        "english_signal",
        "german_risk_signal",
        "reasons",
        "link"
    ]].head(20).to_string(index=False))

if __name__ == "__main__":
    main()