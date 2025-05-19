import smtplib
import json
from email.message import EmailMessage
from datetime import datetime, timedelta
import os

def load_birthdays(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = os.environ["EMAIL_USER"]
    msg["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(os.environ["EMAIL_USER"], os.environ["EMAIL_PASS"])
        server.send_message(msg)

def check_and_send_reminders():
    today = datetime.utcnow().date()
    data = load_birthdays("birthdays.json")

    for entry in data:
        name = entry["name"]
        email = entry["email"]
        bday = datetime.strptime(entry["date"], "%Y-%m-%d").date()

        for hours in [24, 12]:
            target_day = bday - timedelta(hours=hours)
            if today == target_day:
                time_left = f"{hours} hours"
                subject = f"Upcoming Birthday Reminder: {name}"
                body = f"Hi! Just a reminder: {name}'s birthday is in {time_left}."
                send_email(email, subject, body)

if __name__ == "__main__":
    check_and_send_reminders()
