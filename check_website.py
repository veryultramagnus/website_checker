import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import os

URL = "https://example.com"

SMTP_SERVER = "mail.smtp2go.com"
SMTP_PORT = 587
EMAIL = os.getenv("SMTP2GO_USERNAME")
PASSWORD = os.getenv("SMTP2GO_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

def check_website():
    try:
        response = requests.get(URL, timeout=10)
        if response.status_code == 200:
            return f"{URL} is UP (status 200)"
        else:
            return f"{URL} returned status {response.status_code}"
    except Exception as e:
        return f"{URL} check failed: {e}"

def send_email(message):
    msg = MIMEText(message)
    msg["Subject"] = f"Website Status Report - {datetime.now().strftime('%Y-%m-%d')}"
    msg["From"] = EMAIL
    msg["To"] = TO_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    status = check_website()
    send_email(status)
