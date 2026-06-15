import pandas as pd


COMPANY_CAREER_SEARCHES = [
    {
        "company": "ING",
        "country_focus": "Germany / Netherlands / Romania",
        "best_for": "Data Analyst, Business Analyst, Risk, Finance Analytics",
        "search_url": "https://careers.ing.com/en/search-jobs",
        "recommended_keywords": "Data Analyst, Business Analyst, Risk Analyst, KYC, AML"
    },
    {
        "company": "Deutsche Bank",
        "country_focus": "Germany / Luxembourg / Global",
        "best_for": "Technology, Data & Innovation, Risk, Operations, Business Analyst",
        "search_url": "https://careers.db.com/professionals/search-roles/",
        "recommended_keywords": "Data Analyst, Business Analyst, Risk, Operations, Reporting"
    },
    {
        "company": "Commerzbank",
        "country_focus": "Germany / Poland",
        "best_for": "Banking operations, Risk, Reporting, Business Analyst",
        "search_url": "https://www.commerzbank.de/group/careers/job-opportunities/",
        "recommended_keywords": "Business Analyst, Data Analyst, Risk, Compliance, Operations"
    },
    {
        "company": "N26",
        "country_focus": "Germany / Spain / Europe",
        "best_for": "Fintech, Data, Risk, Compliance, Operations",
        "search_url": "https://n26.com/en-eu/careers",
        "recommended_keywords": "Data Analyst, Risk, Compliance, Operations, Reporting"
    },
    {
        "company": "Trade Republic",
        "country_focus": "Germany / UK / France",
        "best_for": "Fintech, Data, Risk, Product Operations, Compliance",
        "search_url": "https://traderepublic.com/en-de/about",
        "recommended_keywords": "Data, Analytics, Risk, Compliance, Operations"
    },
    {
        "company": "Revolut",
        "country_focus": "Germany / Poland / Lithuania / Europe",
        "best_for": "Data Analyst, Operations, FinCrime, Risk, Compliance",
        "search_url": "https://www.revolut.com/careers/",
        "recommended_keywords": "Data Analyst, FinCrime, Risk, Compliance, Operations"
    },
    {
        "company": "BNP Paribas",
        "country_focus": "Luxembourg / Germany / France",
        "best_for": "Banking, Data Management, Risk, KYC/AML, Operations",
        "search_url": "https://group.bnpparibas/en/careers/all-job-offers",
        "recommended_keywords": "Data Analyst, Risk Analyst, KYC, AML, Reporting"
    },
    {
        "company": "European Investment Bank",
        "country_focus": "Luxembourg",
        "best_for": "EU banking, data, risk, operations, finance reporting",
        "search_url": "https://www.eib.org/en/about/careers/index",
        "recommended_keywords": "Analyst, Data, Risk, Finance, Reporting"
    },
    {
        "company": "ABN AMRO",
        "country_focus": "Netherlands",
        "best_for": "Data & Analytics, Risk, Operations, Business Analysis",
        "search_url": "https://www.werkenbijabnamro.nl/en/vacancies",
        "recommended_keywords": "Data Analyst, Business Analyst, Risk, Operations"
    },
    {
        "company": "Rabobank",
        "country_focus": "Netherlands",
        "best_for": "Data & Analytics, Data Management, Risk, Compliance",
        "search_url": "https://rabobank.jobs/en/vacancies/",
        "recommended_keywords": "Data Analyst, Business Analyst, Risk, Compliance"
    },
    {
        "company": "UBS",
        "country_focus": "Switzerland / Germany / Luxembourg",
        "best_for": "Banking analytics, risk, operations, reporting",
        "search_url": "https://www.ubs.com/global/en/careers/jobsearch.html",
        "recommended_keywords": "Data Analyst, Business Analyst, Risk Analyst, Reporting"
    },
    {
        "company": "Citi",
        "country_focus": "Germany / Luxembourg / Poland",
        "best_for": "Operations analyst, risk, KYC/AML, banking analyst",
        "search_url": "https://jobs.citi.com/",
        "recommended_keywords": "Operations Analyst, Data Analyst, Risk, KYC, AML"
    },
    {
        "company": "HSBC",
        "country_focus": "Germany / Luxembourg / Switzerland",
        "best_for": "Global banking, risk, operations, compliance, analytics",
        "search_url": "https://www.hsbc.com/careers",
        "recommended_keywords": "Data Analyst, Business Analyst, Risk, Compliance, Operations"
    }
]


def get_company_career_searches():
    return pd.DataFrame(COMPANY_CAREER_SEARCHES)


def format_company_career_message(limit=8):
    df = get_company_career_searches().head(limit)

    message = "Strategic company career searches:\n\n"

    for number, (_, row) in enumerate(df.iterrows(), start=1):
        message += (
            f"{number}. {row['company']}\n"
            f"Focus: {row['country_focus']}\n"
            f"Best for: {row['best_for']}\n"
            f"Search keywords: {row['recommended_keywords']}\n"
            f"Link: {row['search_url']}\n\n"
        )

    return message


if __name__ == "__main__":
    df = get_company_career_searches()
    print(df.to_string(index=False))