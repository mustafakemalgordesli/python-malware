from email.message import EmailMessage
import os
import ssl
import smtplib
import mimetypes

from os import environ as env
from dotenv import load_dotenv

load_dotenv()

mail_address = env["MAIL_ADDRESS"]
mail_password = env["MAIL_PASSWORD"]


context = ssl.create_default_context()

def attach_file_to_email(email, filename):
    """Attach a file identified by filename, to an email message"""
    with open(filename, 'rb') as fp:
        file_data = fp.read()
        maintype, _, subtype = (mimetypes.guess_type(filename)[0] or 'application/octet-stream').partition("/")
        email.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=filename)



def sendmail(subject, message=None, files=None, send_to=None):
    em = EmailMessage()
    em["From"] = mail_address
    if(not send_to):
        send_to = mail_address
    em['To'] = send_to
    em["Subject"] = subject
    if(message):
        em.set_content(str(message))
    for file in files:
        attach_file_to_email(em, file)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(mail_address, mail_password)
        smtp.sendmail(mail_address, send_to, em.as_string())
        smtp.quit()


