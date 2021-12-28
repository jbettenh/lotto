import os.path
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import yaml


def load_config():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'config_email.yaml')

    if not os.path.exists(filename):
        return "emailnotfound@lotto_picker.com"

    with open("config_email.yaml", 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        return cfg['email_sender']


def send_email(email_receiver, email_subject, email_text, email_html):
    port = 465
    email_sender = load_config()
    password = input('Enter your email password:  ')

    message = MIMEMultipart("alternative")
    message["Subject"] = email_subject
    message["From"] = email_sender
    message["To"] = email_receiver

    text = email_text
    html = email_html

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email_sender, password)
        server.sendmail(email_sender, email_receiver, message.as_string())
