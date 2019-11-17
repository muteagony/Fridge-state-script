import smtplib
""" from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText """

server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()

server.login("username", "password")

server.sendmail("sender", "receiver", "message")
