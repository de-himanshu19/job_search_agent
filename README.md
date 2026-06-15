# Job Search Agent

A Python-based job search agent that searches relevant analyst jobs, filters unsuitable roles, scores jobs based on my profile, and sends the best matches to Telegram.

## Features

- Searches Arbeitsagentur job listings
- Targets Data Analyst, Business Analyst, Risk Analyst, Compliance, KYC/AML, Reporting, and Operations roles
- Filters out jobs requiring fluent/business German
- Scores jobs based on banking, finance, data, SQL, reporting, SAP, compliance, and operations relevance
- Sends top matched jobs to Telegram
- Tracks already sent jobs to avoid duplicate alerts
- Can be scheduled using Windows Task Scheduler

## My Target Profile

This project is designed around my transition into data/business analyst roles, combining:

- 7 years of banking operations experience at Punjab National Bank
- Experience in AML/KYC, reporting, branch operations, loan recovery, and customer data handling
- Application testing and technical support experience at Giesecke+Devrient
- Current upskilling in Data Analytics, SQL, Python, dashboards, and automation

## Tech Stack

- Python
- Pandas
- Requests
- Python-dotenv
- Telegram Bot API
- Windows Task Scheduler

## Setup

1. Install dependencies:

```bash
pip install requests pandas python-dotenv