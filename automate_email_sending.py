''' You work at a company that sends daily reports to clients via email. The goal of this project
 is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:
    Use the smtplib library to connect to the email server and send the emails.
    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.
    Use the os library to access the report files that need to be sent.
    Use a for loop to iterate through the list of recipients and send the email and attachment.
    Use the schedule library to schedule the script to run daily at a specific time.
    You can also set up a log file to keep track of the emails that have been sent and any
    errors that may have occurred during the email sending process. '''


import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import schedule
from dotenv import load_dotenv


# Assumes you have created a .env file with SMTP_USER and SMTP_PASSWORD
load_dotenv()  # take environment variables from .env.


REPORT_PATH = 'customer_report.pdf'

RECIPIENTS = [
    "A Test User <to@example.com>",
    "A Test User <the@example.com>"
]


EMAIL_SUBJECT = "Daily Report"
EMAIL_BODY = "Please see attached pdf."
SENDER = "Company Email <from@example.com>"
SMTP_USER = os.environ.get('SMTP_USER')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')


def send_report(
        recipient: str, sender_email: str, email_subject: str, email_body: str, report_path: str
    ):
    """
    Send report to recipient via email.
    """
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = email_subject
    message.attach(MIMEText(email_body, "plain"))
    with open(report_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {report_path}",
    )
    message.attach(part)
    text = message.as_string()
    if SMTP_USER and SMTP_PASSWORD:
        with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(sender_email, recipient, text)
    else:
        print('SMTP Credentials need to be set in the .env file.')


def send_customer_reports():
    """
    Assumes that a customer.pdf file exists
    """
    print('==== Sending out reports')
    if os.path.exists(REPORT_PATH):
        for email in RECIPIENTS:
            send_report(email, SENDER, EMAIL_SUBJECT, EMAIL_BODY, REPORT_PATH)
        print('==== Done Sending reports.')
    else:
        print('Customer report not found')


# schedule email to go out at 5:30pm everyday.
schedule.every().day.at("17:52").do(send_customer_reports)


while True:
    schedule.run_pending()
