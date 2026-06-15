import json
import os

SENT_JOBS_FILE = "sent_jobs.json"


def load_sent_jobs():
    if not os.path.exists(SENT_JOBS_FILE):
        return set()

    with open(SENT_JOBS_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return set(data)


def save_sent_jobs(sent_jobs):
    with open(SENT_JOBS_FILE, "w", encoding="utf-8") as file:
        json.dump(list(sent_jobs), file, indent=4, ensure_ascii=False)


def filter_new_jobs(df):
    sent_jobs = load_sent_jobs()

    if df.empty:
        return df

    new_df = df[~df["ref"].isin(sent_jobs)].copy()

    return new_df


def mark_jobs_as_sent(df):
    sent_jobs = load_sent_jobs()

    for _, row in df.iterrows():
        ref = row.get("ref")
        if ref:
            sent_jobs.add(ref)

    save_sent_jobs(sent_jobs)