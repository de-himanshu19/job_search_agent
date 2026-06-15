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
