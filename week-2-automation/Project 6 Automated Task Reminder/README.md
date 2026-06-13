Project 6 — Automated Task Reminder System
Week: 2 — Day 13

Date: 2026-06-13

Tools: Zapier, Google Sheets, Gmail

Status: ✅ Completed

Time to build: 25 minutes (built twice due to configuration adjustment)

What This Project Does
This automation runs every morning at 7 AM automatically without any manual trigger. It reads all pending tasks from a Google Sheet and sends a personalized Gmail reminder listing the tasks, due dates, and current status. Every morning you wake up with a clear reminder of exactly what needs to be done that day.

Real World Use Case
Most people forget tasks because they rely on memory. This system eliminates that problem completely. Every morning at 7 AM — before the day gets busy — a reminder arrives in your inbox with your exact task list pulled directly from your Google Sheet.
This system is used by:

Freelancers managing multiple client deadlines
Small business owners tracking daily operations
Students managing assignment due dates
Project managers tracking team deliverables
Anyone who wants a reliable automated accountability system

This is also a sellable service. Small businesses and solopreneurs pay for personalized reminder and task management automations.

Tools Used
ToolPurposeSchedule by ZapierFires the automation every day at 7 AM automaticallyGoogle SheetsStores all tasks with due dates and statusGmailSends the daily reminder email automatically

How It Works — The Logic
Every day at 7:00 AM
        ↓
Schedule by Zapier fires automatically
        ↓
Zapier reads tasks from Google Sheet
        ↓
Gmail sends personalized reminder email
This follows time based automation logic:

Scheduled Trigger → Data Read → Automated Notification

Google Sheet Structure
Created spreadsheet named "Task Reminder System" with four columns:
Column AColumn BColumn CColumn DTask NameDue DateEmailStatus
Test tasks added:
Task NameDue DateEmailStatusComplete Python Setup2026-06-15safdar@email.comPendingUpload Week 2 Projects2026-06-13safdar@email.comPendingWrite Week 2 Recap Post2026-06-14safdar@email.comPending
Status system:

Pending — task not yet completed
Completed — task done, stays in sheet for records


Step by Step Build Process
Step 1 — Create Google Sheet

Created new Google Sheet named "Task Reminder System"
Added four column headers — Task Name, Due Date, Email, Status
Added three real test tasks with actual due dates
Set all statuses to Pending

Step 2 — Create New Zap

Opened Zapier → clicked "Create Zap"
Named the Zap: Automated Task Reminder

Step 3 — Set Up Schedule Trigger

Searched: "Schedule by Zapier"
Selected: "Every Day"
Set time: 7:00 AM
This fires the automation automatically every morning without any manual action required
Clicked "Continue"

Note: Schedule by Zapier does not fire during testing — it only fires at the exact time set. To test manually click "Run" at the top of the Zap editor to force it to fire immediately.
Step 4 — Add Google Sheets Action

Clicked "+" to add action
Searched: Google Sheets
Selected: "Get Many Rows"
Connected Google account
Selected "Task Reminder System" spreadsheet
Selected Sheet1
Left Row ID empty to read all rows
Clicked "Test Action"
Confirmed all three task rows detected correctly

Step 5 — Add Gmail Action

Clicked "+" to add action
Searched: Gmail
Selected: "Send Email"
Configured email:

To: Email column from Google Sheet
Subject: Daily Task Reminder — (Task Name from sheet)
Body: personalized reminder with task name, due date, and status mapped from sheet


Clicked "Test Action"
Confirmed email arrived correctly in Gmail

Step 6 — Publish

Clicked "Publish Zap"
Zap set to fire every morning at 7 AM automatically


Challenges Faced and How I Solved Them
Challenge 1 — Built the automation twice

First attempt had incorrect configuration. Instead of continuing to debug the same Zap — deleted it and rebuilt from scratch. Second build was faster and cleaner because the logic was already understood from the first attempt.
Lesson learned: Sometimes rebuilding from scratch is faster than debugging a broken foundation. Real developers do this too.
Challenge 2 — Setting the correct time for email sending

Configuring the Schedule by Zapier trigger to fire at the exact right time required understanding how time zones work in Zapier. After adjusting the settings correctly the schedule was set to 7 AM successfully.
Challenge 3 — Email not arriving during testing

Discovered that Schedule by Zapier does not fire during normal testing — it only fires at the scheduled time. Used the manual "Run" button to force immediate firing for testing purposes.

What I Learned
Technical lessons:

How to use Schedule by Zapier as a time based trigger
The difference between event based triggers and time based triggers
How to read multiple rows from Google Sheets in one Zapier action
How to map Google Sheet columns to Gmail email fields dynamically
Schedule triggers only fire at set time — use Run button for manual testing

Mindset lessons:

Rebuilding from scratch is sometimes the fastest solution
25 minutes to build a time based automation shows real speed improvement over Week 2
Every project this week was faster than the last — that is measurable skill growth

Week 2 Speed Progression:

Project 1 — needed full guidance, took hours
Project 2 — Make.com, multiple errors, long debugging
Project 3 — 30 minutes, zero errors
Project 4 — 53 minutes, solved errors independently
Project 5 — 33 minutes, solved issues independently
Project 6 — 25 minutes, built twice, still fast


Key Concepts Demonstrated
Time Based Automation — triggering a workflow automatically at a scheduled time every day without any manual action
Schedule by Zapier — Zapier's built in scheduler that replaces the need for an external trigger app
Automated Accountability System — using automation to replace manual checking and memory with a reliable daily system
Data to Email Pipeline — reading structured data from a spreadsheet and converting it into a personalized email automatically

Screenshot
(See screenshot files in this folder)

Next Project
Week 3 starts Day 15 — Python Basics

Variables, loops, functions, APIs, and first Python scripts.

This project is part of my AI Skills Journey — a 30-day structured learning plan building real automation skills from zero.
GitHub: github.com/safdar1234k/AI-Skills-Journey
