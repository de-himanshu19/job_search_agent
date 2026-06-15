BANKING_COMPANIES = [
    "bank",
    "deutsche bank",
    "commerzbank",
    "ing deutschland",
    "ing bank",
    "targobank",
    "landesbank",
    "lbbw",
    "dkb",
    "aareal",
    "creditplus",
    "sparkasse",
    "volksbank",
    "finanz informatik",
    "allianz",
    "ergo",
    "axa",
    "r+v",
    "flossbach",
    "deutsche pfandbriefbank",
    "atrivia",
    "atriuvia",
    "n26",
    "trade republic",
    "revolut"
]

GOOD_TITLE_KEYWORDS = [
    "data analyst",
    "data-analyst",
    "datenanalyst",
    "business analyst",
    "business-analyst",
    "reporting analyst",
    "risk analyst",
    "risikoanalyst",
    "financial analyst",
    "finanzanalyst",
    "data quality analyst",
    "process analyst",
    "prozessanalyst",
    "operations analyst",
    "compliance",
    "kyc",
    "aml",
    "geldwäsche",
    "fraud analyst",
    "controller",
    "controlling"
]

GOOD_PROFILE_KEYWORDS = [
    "sql",
    "excel",
    "sap",
    "reporting",
    "berichtswesen",
    "finance",
    "financial",
    "finanz",
    "bank",
    "banking",
    "risk",
    "risiko",
    "compliance",
    "kyc",
    "aml",
    "geldwäsche",
    "data",
    "daten",
    "analytics",
    "business",
    "process",
    "prozess",
    "operations"
]

GOOD_CITIES = [
    "frankfurt",
    "berlin",
    "munich",
    "münchen",
    "hamburg",
    "düsseldorf",
    "stuttgart",
    "köln",
    "bonn",
    "hannover",
    "münster",
    "nürnberg"
]
ENGLISH_POSITIVE_KEYWORDS = [
    "english",
    "englisch",
    "gute englischkenntnisse",
    "sehr gute englischkenntnisse",
    "very good english",
    "fluent english",
    "international",
    "international team",
    "global",
    "multinational"
]

GERMAN_RISK_KEYWORDS = [
    "kundenberatung",
    "telefonische kundenbetreuung",
    "privatkunden",
    "firmenkundenberatung",
    "filialgeschäft",
    "sachbearbeiter",
    "kundenservice",
    "beratungsgespräche",
    "schriftliche und telefonische kommunikation"
]

def calculate_score(job):
    score = 0
    reasons = []

    title = job.get("title", "").lower()
    company = job.get("company", "").lower()
    city = job.get("city", "").lower()
    profession = job.get("profession", "").lower()
    search_role = job.get("search_role", "").lower()
    english_signal = job.get("english_signal", False)
    german_risk_signal = job.get("german_risk_signal", False)

    combined = f"{title} {company} {city} {profession} {search_role}"

    for keyword in GOOD_TITLE_KEYWORDS:
        if keyword in title:
            score += 25
            reasons.append(f"title: {keyword}")
            break

    for keyword in BANKING_COMPANIES:
        if keyword in company:
            score += 30
            reasons.append(f"bank/finance company: {keyword}")
            break

    profile_hits = []
    for keyword in GOOD_PROFILE_KEYWORDS:
        if keyword in combined:
            profile_hits.append(keyword)

    if profile_hits:
        score += min(len(profile_hits) * 5, 25)
        reasons.append("profile keywords: " + ", ".join(profile_hits[:5]))

    for city_keyword in GOOD_CITIES:
        if city_keyword in city:
            score += 10
            reasons.append(f"good city: {city_keyword}")
            break

    if "data-analyst" in profession or "business-analyst" in profession:
        score += 10
        reasons.append("official profession match")
        
    if english_signal:
        score += 20
        reasons.append("English-friendly signal found in job details")

    if german_risk_signal:
        score -= 15
        reasons.append("German-heavy customer-facing signal")

    return score, " | ".join(reasons)