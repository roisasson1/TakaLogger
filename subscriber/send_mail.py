import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def call(i_site, i_error):
    smtp_user = "parkomat@zohomail.com"
    smtp_password = "roson9388"
    server = "smtp.zoho.com"
    message = i_error

    port = 587
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f'תקלה באתר: {i_site}'
    msg["From"] = smtp_user
    msg["To"] = "roiy100000@gmail.com"
    msg.attach(MIMEText(message, "plain"))
    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.login(smtp_user, smtp_password)
    s.sendmail(smtp_user, "roiy100000@gmail.com", msg.as_string())
