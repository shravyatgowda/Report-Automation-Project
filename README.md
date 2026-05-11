Report Automation Project

This project automates data cleaning, SQL query execution, and email reporting. It is modular, secure, and designed to run via Anaconda Prompt or be scheduled using batch scripts / Task Scheduler

📁 Folder Structure
Report/
├── configs/
│   ├── auto_email.py
│   ├── email_template.py
│   └── user_pwrd.py
│
├── utils/
│   ├── data_cleaning.py
│   └── query.py
│
├── main.py
├── run_with_failure_msg.py
├── run_with_scheduler.bat
└── README.md
⚙️ Setup Instructions (Anaconda Prompt)

1. Open Anaconda Prompt
Launch Anaconda Prompt from your Start Menu.

2. Create and Activate Environment
conda create -n Report_Automation python=3.10 -y
conda activate Report_Automation

3. Install Required Packages
pip install pandas keyring

4. Set Up Email Credentials Securely
import keyring
keyring.set_password("gmail", "user@example.com", "your_password")

5. Ensure SQLite Database Exists
Create example.db with a users table if needed:
sqlite3 example.db
CREATE TABLE users (name TEXT, age INTEGER);



🚀 Running the Project
Run Main Script
python Report/main.py


Run with Error Handling
python Report/main.py


Run via Batch Scheduler
cd "C:\\Working Directory\\Review Report Automation"
run_with_scheduler.bat


🧹 Features
Data Cleaning: whitespace removal, case standardization, duplicate handling
SQL Queries: dynamic generation and execution
Email Reports: SMTP-based email delivery with secure credentials
Error Notifications: automatic email alerts on failure
Scheduling: batch script for automation via Task Scheduler

