import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'alaiminassim@gmail.com'
email_password = 'lgfgfmptxrslfukp' # os.environ.get('EMAIL_PASSWORD')
email_receiver = 'alaiminassim@gmail.com'

subject = 'Test email'
body = 'This is a test email'

def send_email(Sender, Password, Receiver, Subject, Body):
    em = EmailMessage()
    em['From'] = Sender
    em['To'] = Receiver
    em['Subject'] = Subject
    em.set_content(Body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(Sender, Password)
        smtp.sendmail(Sender, Receiver, em.as_string())

send_email(email_sender, email_password, email_receiver, subject, body)
