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

## Project Structure

```text
job_search_agent/
│
├── config.py
├── job_history.py
├── job_scorer.py
├── run_daily_job_agent.py
├── search_arbeitsagentur.py
├── search_company_careers.py
├── send_test_message.py
├── telegram_sender.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Download and Set Up the Project

### Step 1: Clone the repository

Open PowerShell or VS Code terminal and run:

```bash
git clone https://github.com/YOUR_USERNAME/job_search_agent.git
```

Then move into the project folder:

```bash
cd job_search_agent
```

Replace `YOUR_USERNAME` with your GitHub username.

Example:

```bash
git clone https://github.com/de-himanshu19/job_search_agent.git
cd job_search_agent
```

---

### Step 2: Create a virtual environment

Run:

```bash
python -m venv venv
```

---

### Step 3: Activate the virtual environment

For Windows PowerShell:

```bash
venv\Scripts\activate
```

After activation, you should see something like:

```text
(venv) PS C:\...\job_search_agent>
```

---

### Step 4: Install required packages

Run:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install requests pandas python-dotenv
```

---

## Telegram Bot Setup

### Step 1: Create a Telegram bot

1. Open Telegram
2. Search for `BotFather`
3. Send:

```text
/newbot
```

4. Follow the instructions
5. Copy the bot token

The token looks like this:

```text
123456789:ABCxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### Step 2: Get your Telegram Chat ID

1. Send a message like `Hello` to your new Telegram bot
2. Open this link in your browser:

```text
https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
```

Replace `YOUR_BOT_TOKEN` with your actual bot token.

3. Find the `chat` section and copy the `id`

Example:

```text
"chat":{"id":123456789}
```

---

## Create `.env` File

In the main project folder, create a file named:

```text
.env
```

Add your Telegram details:

```text
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
```

Important: Do not upload `.env` to GitHub because it contains private credentials.

---

## Test Telegram Connection

Run:

```bash
python send_test_message.py
```

If everything is correct, you should receive a test message in Telegram.

---

## Run the Full Job Search Agent

Run:

```bash
python run_daily_job_agent.py
```

The script will:

1. Search jobs from Arbeitsagentur
2. Remove duplicate jobs
3. Filter jobs requiring fluent/business German
4. Score jobs based on profile relevance
5. Send top matched jobs to Telegram
6. Save sent jobs in local history

---

## Schedule the Agent with Windows Task Scheduler

### Step 1: Find Python path

In PowerShell, run:

```powershell
where.exe python
```

Example Python path:

```text
C:\Python314\python.exe
```

---

### Step 2: Open Task Scheduler

1. Press Windows key
2. Search `Task Scheduler`
3. Open it
4. Click `Create Basic Task`

---

### Step 3: Create the task

Task name:

```text
Daily Job Search Agent
```

Trigger:

```text
Daily
```

Time example:

```text
08:00
```

Action:

```text
Start a program
```

Program/script:

```text
C:\Python314\python.exe
```

Add arguments:

```text
"run_daily_job_agent.py"
```

Start in:

```text
C:\Users\YOUR_USERNAME\Desktop\personal projects\job_search_agent
```

Example:

```text
C:\Users\himan\Desktop\personal projects\job_search_agent
```

---

### Step 4: Recommended Task Scheduler settings

In the task properties:

General tab:

```text
Run only when user is logged on
```

Settings tab:

```text
Allow task to be run on demand
Run task as soon as possible after a scheduled start is missed
If the task fails, restart every 1 minute
Attempt to restart up to 3 times
```

Conditions tab:

Untick:

```text
Start the task only if the computer is on AC power
```

---

### Step 5: Test the scheduled task

In Task Scheduler:

1. Select `Daily Job Search Agent`
2. Click `Run`
3. Wait 1–2 minutes
4. Check Telegram

If successful, the task is ready for daily use.

---

## Important Files Not Uploaded to GitHub

These files should not be uploaded:

```text
.env
sent_jobs.json
__pycache__/
*.pyc
job_agent_log.txt
```

They are ignored using `.gitignore`.

---

## `.gitignore` Content

The `.gitignore` file should contain:

```gitignore
.env
__pycache__/
*.pyc
sent_jobs.json
job_agent_log.txt
venv/
```

---

## `requirements.txt` Content

The `requirements.txt` file should contain:

```text
requests
pandas
python-dotenv
```

---

## How to Upload This Project to GitHub

### Step 1: Create a new GitHub repository

1. Open GitHub
2. Click `New repository`
3. Repository name:

```text
job_search_agent
```

4. Keep it public or private
5. Do not add README, `.gitignore`, or license from GitHub
6. Click `Create repository`

---

### Step 2: Initialize Git locally

In VS Code terminal, inside the project folder, run:

```bash
git init
```

Check status:

```bash
git status
```

---

### Step 3: Add files

```bash
git add .
```

Check again:

```bash
git status
```

Make sure `.env` is not included.

---

### Step 4: Commit files

```bash
git commit -m "Initial version of job search agent"
```

---

### Step 5: Connect local project with GitHub

Replace the URL with your actual GitHub repository URL:

```bash
git remote add origin https://github.com/YOUR_USERNAME/job_search_agent.git
```

Set branch name:

```bash
git branch -M main
```

Push to GitHub:

```bash
git push -u origin main
```

---

## Project Logic and Workflow

This project works as a local Python-based job search automation tool. The main goal is to search jobs from the German Arbeitsagentur API, filter unsuitable jobs, score the remaining jobs based on profile relevance, and send the best job matches to Telegram.

The project follows this workflow:

```text
Search Keywords
      ↓
Arbeitsagentur Search API Request
      ↓
Parse JSON Search Results
      ↓
Clean and Remove Duplicates
      ↓
Fetch Full Job Details
      ↓
Check German Language Requirements
      ↓
Check English-Friendly Signals
      ↓
Score Jobs
      ↓
Remove Already-Sent Jobs
      ↓
Send Top Jobs to Telegram
      ↓
Save Sent Jobs History
```

---

## 1. Configuration

The file `config.py` contains the main search settings.

It includes:

* Target job titles such as Data Analyst, Business Analyst, Risk Analyst, Compliance Analyst, KYC Analyst, AML Analyst, and Reporting Analyst
* German search terms such as Datenanalyst, Risikoanalyst, Geldwäsche, Berichtswesen, and Finanzdienstleistungen
* Positive keywords related to banking, finance, SQL, Excel, SAP, reporting, KYC, AML, compliance, and operations
* Negative keywords for jobs that are not suitable, such as software developer roles or roles requiring very high German language skills

This allows the project to search for jobs that match a banking, finance, data, reporting, compliance, and operations profile.

---

## 2. Job Search Request

The main job search happens in `search_arbeitsagentur.py`.

For every role defined in `TARGET_ROLES`, the script sends a request to the Arbeitsagentur Jobsuche API.

The request is made using:

```python
response = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=20)
```

Here:

* `BASE_URL` is the Arbeitsagentur search API endpoint
* `HEADERS` contains the API key/header required by the API
* `params` contains search parameters such as keyword, location, job type, page size, and published date range
* `timeout=20` prevents the script from waiting forever if the API does not respond

After the request is successful, the response is parsed using:

```python
data = response.json()
```

This converts the API JSON response into a Python dictionary.

The job list is extracted from:

```python
data.get("ergebnisliste", [])
```

So the search results are not manually created. They are downloaded from the Arbeitsagentur API and parsed by the script.

---

## 3. Job Data Extraction

After the search API returns results, the script extracts useful job information from each job.

The extracted fields include:

* Job title
* Company name
* City/location
* Publication date
* Profession
* Job reference number
* Job link
* Search role that found the job

These extracted jobs are stored in a Pandas DataFrame.

A DataFrame is used because it makes it easier to clean, filter, score, sort, and display job results.

---

## 4. Basic Cleaning and Duplicate Removal

After collecting jobs from multiple search terms, some jobs may appear more than once.

For example, the same job may appear under both:

```text
Data Analyst
Business Analyst
Reporting
```

To avoid sending duplicate jobs, the script removes duplicates using the job reference number.

The script also applies a basic negative keyword filter to remove clearly unsuitable jobs, such as roles focused on software development or roles requiring very high German language skills.

---

## 5. Fetching Full Job Details

The search API gives basic job information, but it may not contain the full job description.

Therefore, the script makes a second API request for each job using the job reference number.

First, the job reference number is encoded. Then the detail URL is created:

```python
url = f"{DETAIL_BASE_URL}/{encoded_ref}"
```

The job detail request is made using:

```python
response = requests.get(url, headers=HEADERS, timeout=20)
```

If the API response is successful, the full JSON response is parsed:

```python
data = response.json()
```

Then the full job detail JSON is converted into lowercase searchable text:

```python
detail_text = json.dumps(data, ensure_ascii=False).lower()
```

This makes it easier to search inside the complete job description for language requirements and other important signals.

---

## 6. German Language Filtering

The function `filter_german_fluent_jobs()` checks the full job detail text.

It searches for phrases that indicate the job requires fluent, business-level, C1, C2, or native-level German.

Examples of blocked phrases include:

```text
fließend Deutsch
verhandlungssicher Deutsch
Deutsch C1
Deutsch C2
native German
fluent German
sehr gute Deutschkenntnisse
```

If any of these phrases are found in the full job detail text, the job is removed.

This is important because the project is designed for a candidate with English fluency and basic/intermediate German learning progress, not for roles requiring fluent German.

---

## 7. English-Friendly and German-Risk Signals

After filtering out jobs with strong German requirements, the script checks for two types of signals.

### English-Friendly Signals

The script checks whether the job detail contains words such as:

```text
English
Englisch
international
global
multinational
international team
```

If these signals are found, the job receives a positive score boost.

### German-Heavy Risk Signals

The script also checks whether the job looks customer-facing or German-heavy.

Examples include:

```text
Kundenberatung
Kundenservice
telefonische Kundenbetreuung
direkter Kundenkontakt
Firmenkundenberatung
Privatkundenberatung
```

These jobs are not always removed, but they receive a score penalty because they may require stronger spoken German.

---

## 8. Job Scoring Logic

The scoring logic is stored in `job_scorer.py`.

The function `calculate_score()` receives one job as a dictionary and returns:

```text
score
reasons
```

The score is based on several factors:

* Job title match
* Banking or finance company match
* Profile keyword match
* Good city match
* Official profession match
* English-friendly signal
* German-heavy customer-facing risk

For example, a job may receive points if the title contains:

```text
Data Analyst
Business Analyst
Risk Analyst
Compliance
KYC
AML
Reporting
```

It may also receive points if the company or profession is related to banking, finance, risk, compliance, or operations.

The function also creates explanation text called `reasons`, which explains why the job received its score.

Example reason:

```text
title: risk analyst | bank/finance company: bank | profile keywords: reporting, bank, risk | English-friendly signal found in job details
```

This makes the scoring transparent and easy to understand.

---

## 9. Applying the Score to All Jobs

Each job row in the DataFrame is passed to the scoring function.

The script converts each row into a dictionary and sends it to `calculate_score()`.

The returned score and reason are stored in two new DataFrame columns:

```text
score
reasons
```

This allows the script to sort jobs by score and select the best matches.

---

## 10. Already-Sent Job Tracking

The file `job_history.py` manages duplicate tracking across different runs.

The project uses a local file called:

```text
sent_jobs.json
```

This file stores job reference numbers that were already sent to Telegram.

Before sending new jobs, the script checks whether a job reference number already exists in `sent_jobs.json`.

If the job was already sent before, it is skipped.

This prevents the same job from being sent repeatedly every day.

---

## 11. Telegram Notification

The file `telegram_sender.py` manages Telegram communication.

The Telegram bot token and chat ID are stored in a local `.env` file:

```text
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

The script sends a message using the Telegram Bot API.

The message includes:

* Top matched jobs
* Company name
* City
* Score
* Job link

The request is sent using:

```python
response = requests.post(url, data=payload, timeout=20)
```

If Telegram returns a successful response, the script marks those jobs as sent.

If Telegram sending fails, the jobs are not marked as sent.

This prevents losing job results when there is an error.

---

## 12. Daily Runner File

The file `run_daily_job_agent.py` is the main runner file.

It calls the main job search function:

```python
from search_arbeitsagentur import main

if __name__ == "__main__":
    print("Starting daily job search agent...")
    main()
    print("Daily job search agent completed.")
```

This file is useful because it gives one simple entry point for running the whole project.

Instead of running multiple files manually, the user can simply run:

```bash
python run_daily_job_agent.py
```

---

## 13. Scheduling

The project can be scheduled using Windows Task Scheduler.

The scheduled task runs:

```text
python run_daily_job_agent.py
```

This allows the job agent to run automatically every morning.

The local system must be turned on and connected to the internet for the scheduled task to run.

---

## 14. Function Summary

| File                        | Main Purpose                                                                              |
| --------------------------- | ----------------------------------------------------------------------------------------- |
| `config.py`                 | Stores search roles, keywords, negative keywords, and target settings                     |
| `search_arbeitsagentur.py`  | Searches jobs, parses API results, filters jobs, scores jobs, and sends Telegram messages |
| `job_scorer.py`             | Calculates job match score and explains the scoring reasons                               |
| `job_history.py`            | Tracks already-sent jobs using `sent_jobs.json`                                           |
| `telegram_sender.py`        | Sends job results to Telegram                                                             |
| `search_company_careers.py` | Stores strategic company career links for future improvement                              |
| `send_test_message.py`      | Tests whether Telegram setup is working                                                   |
| `run_daily_job_agent.py`    | Main entry point for running the full job search agent                                    |

---

## 15. Overall Summary

This project does not manually assign jobs.

The script automatically requests job data from the Arbeitsagentur API, parses the JSON response, extracts job information, fetches full job details, filters unsuitable jobs, scores the remaining jobs using a profile-based scoring framework, removes already-sent jobs, and sends the best matches to Telegram.

The scoring framework is manually designed, but it is applied to real job data downloaded from the API.


## Notes

This project currently runs locally on Windows. It will not run if the computer is fully powered off.

For future improvement, this project can be deployed to:

* GitHub Actions
* PythonAnywhere
* Google Cloud
* AWS
* VPS server

---

## Disclaimer

This project is for personal job search support and learning purposes. It does not automatically apply to jobs.
