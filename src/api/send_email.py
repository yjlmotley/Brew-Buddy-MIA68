import smtplib
from email.message import EmailMessage
import os

MAIL_SERVER="smtp.gmail.com"
#replace with your email providers smtp server if needed
MAIL_PORT=465 #TLS PORT
MAIL_USE_TLS = True
MAIL_USERNAME= os.getenv("GMAIL_EMAIL") #Email that sends forgot email reset password
MAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

def send_email(recipient, body, subject):
    try: 
        with smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT) as server:
            server.login(MAIL_USERNAME, MAIL_PASSWORD)
            smg = EmailMessage()
            smg["Subject"]= subject
            smg["From"]= MAIL_USERNAME
            smg["To"]= recipient
            smg.set_content(body)
            server.send_message(smg)
    except smtplib.SMTPException as e: 
        #log the exception e
        raise Exception(f"failed to send email: {str(e)}")
