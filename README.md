# 🎉 Birthday Reminder App

Automatically sends email reminders 24 and 12 hours before a birthday.

## 📁 Files

- `birthdays.json` – Stores birthday data.
- `birthday_reminder.py` – Script to check birthdays and send emails.
- `.github/workflows/reminder.yml` – GitHub Actions workflow for automation.

## 🔧 Setup

1. **Fork and clone this repository**

2. **Create GitHub Secrets:**

Go to your repo → Settings → Secrets → Actions → `New repository secret`:

- `EMAIL_USER` – Your email (e.g., Gmail address)
- `EMAIL_PASS` – App password (not your Gmail login password)

> 💡 If using Gmail, enable 2FA and create an [App Password](https://support.google.com/accounts/answer/185833).

3. **Customize `birthdays.json`**

Add your own contacts with `name`, `email`, and `date` (in `YYYY-MM-DD` format).

4. **Automation via GitHub Actions**

This script will run automatically **twice a day** and email you reminders 24h and 12h before a birthday.

## 📧 Email Preview

> Subject: `Upcoming Birthday Reminder: Alice`  
> Body: `Hi! Just a reminder: Alice's birthday is in 24 hours.`

## 💡 Tips

- Set your own email as the recipient in `birthdays.json` if you want all reminders to come to you.
