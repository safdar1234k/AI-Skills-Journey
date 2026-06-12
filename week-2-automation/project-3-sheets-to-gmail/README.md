Project 3 — Google Sheets → Gmail Notification Automation
Week: 2 — Day 12

Date: 2026-06-12

Tool: Zapier

Status: ✅ Completed

Time to build: 30 minutes

What This Project Does
This automation monitors a Google Sheets spreadsheet in real time. Every time a new row is added to the spreadsheet — whether manually or through a form submission — Zapier instantly detects it and sends a Gmail notification to the specified email address. Zero manual checking required. Zero delay.

Real World Use Case
Imagine you are a small business owner running a contact form on your website. Every time a potential customer submits their details — name, email, message — those details land in a Google Sheet. Without automation you would have to open that sheet manually every few hours to check for new leads.
With this automation — the moment a new lead arrives you get an instant Gmail notification. You can respond within minutes instead of hours. Faster response = higher chance of closing the client.
This exact workflow is used by:

Small businesses tracking customer inquiries
Freelancers monitoring new project requests
Teachers tracking student form submissions
Event organizers collecting registrations


Tools Used
ToolPurposeZapierAutomation engine connecting both appsGoogle SheetsData source — triggers the automationGmailSends the notification email

How It Works — The Logic
New row added to Google Sheets
            ↓
Zapier detects the new row instantly
            ↓
Zapier reads the data from that row
            ↓
Gmail sends notification email with the row data
This follows the fundamental automation logic:

IF a new row appears in Google Sheets THEN send a Gmail notification.

Step by Step Build Process
Step 1 — Create a New Zap

Opened Zapier at zapier.com
Clicked "Create Zap" button
Named the Zap: Google Sheets to Gmail Notification

Step 2 — Set Up the Trigger

Searched for Google Sheets in the trigger search box
Selected the app Google Sheets
Selected the trigger event: "New Spreadsheet Row"
This means: every time a new row is added — the Zap fires

Step 3 — Connect Google Account

Clicked "Sign in to Google Sheets"
Selected my Google account and allowed Zapier permissions
Zapier confirmed the connection successfully

Step 4 — Configure the Trigger

Selected the correct Spreadsheet from the dropdown
Selected the correct Sheet Tab — Sheet1
Clicked "Continue"

Step 5 — Test the Trigger

Clicked "Test Trigger"
Zapier pulled the most recent row from the spreadsheet
Confirmed all column fields were detected correctly — Name, Email, Timestamp
Clicked "Continue"

Step 6 — Set Up the Action

Clicked "+" to add an Action
Searched for Gmail
Selected "Send Email" as the action event

Step 7 — Connect Gmail Account

Clicked "Sign in to Gmail"
Selected my Google account and allowed permissions
Gmail connection confirmed successfully

Step 8 — Configure the Email

To: my own email address
Subject: New Row Added — Google Sheets Notification
Body: Used Zapier's field mapping to insert live data from the spreadsheet:

Name from the new row
Email from the new row
Timestamp of submission


This means every notification email contains the actual data from that specific row

Step 9 — Test the Action

Clicked "Test Action"
Zapier sent a test email to my Gmail
Opened Gmail — notification email arrived instantly
All data fields appeared correctly in the email body
Zero errors

Step 10 — Publish the Zap

Clicked "Publish Zap"
Zap status changed to ON
Added a new row to Google Sheets manually to confirm live test
Gmail notification arrived within seconds
Automation confirmed working perfectly


What I Learned
Technical lessons:

How to use Google Sheets as a Zapier trigger using "New Spreadsheet Row"
How to map spreadsheet column data into a Gmail email body
How to test both trigger and action separately before publishing
How to verify a live automation after publishing

Mindset lessons:

Automation thinking is getting faster. This project took 30 minutes with zero errors compared to previous projects that took hours
The more automations you build the more you start seeing automation opportunities everywhere
Small automations like this save businesses hours every week — and businesses pay for this

Comparison with previous projects:

Project 1 — Zapier Google Form to Gmail — took longer, needed guidance
Project 2 — Make.com Google Form to Sheets — took hours, multiple errors
Project 3 — Zapier Google Sheets to Gmail — 30 minutes, zero errors
Progress is real and measurable


Key Automation Concepts Demonstrated
Trigger — the event that starts the automation. In this project: new row in Google Sheets.
Action — what happens because of the trigger. In this project: Gmail sends a notification.
Field Mapping — connecting specific data from the trigger to the action. In this project: spreadsheet columns mapped to email body.
Testing — always test trigger and action separately before publishing. Never assume it works — verify it.

Screenshot
(See screenshot file in this folder)

Next Project
Project 4 — AI Content Generation Workflow

Google Form → Zapier → AI Tool → Summary saved to Google Sheets automatically.

This project is part of my AI Skills Journey — a 30-day structured learning plan building from AI fundamentals to automation to Python to portfolio.
GitHub: github.com/safdar1234k/AI-Skills-Journey

Copy this entire thing into your README.md file and upload it with your screenshot.
Come back when uploaded and we start Project 4 immediately. 🔒
