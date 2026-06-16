projects = [
    {"name": "Form to Gmail", "tool": "Zapier", "day": 8, "time": "Full day"},
    {"name": "Make Automation", "tool": "Make.com", "day": 10, "time": "Full day"},
    {"name": "Google Sheets to Gmail", "tool": "Zapier", "day": 12, "time": "30 mins"},
    {"name": "AI Content Generation", "tool": "Zapier + AI", "day": 12, "time": "53 mins"},
    {"name": "Lead Collection System", "tool": "Zapier", "day": 12, "time": "33 mins"},
    {"name": "Task Reminder", "tool": "Zapier", "day": 13, "time": "25 mins"}
]
total_projects = len(projects)
score = 86/100
with open("week 2 projects_report.txt", "w") as report_file:
    report_file.write("WEEK 2 PROJECTS REPORT\n")
    report_file.write("===========================\n")
    for project in projects:
        report_file.write(f" Project name:{project['name']}, Tool used:{project['tool']}, Day: {project['day']},Time taken:{project['time']} \n")
with open("week 2 projects_report.txt", "a") as report_file:
    report_file.write("\n===========================\n")
    report_file.write(f"\nTotal projects completed: {total_projects}\n")
    report_file.write(f"Score: {score*100}%\n")

