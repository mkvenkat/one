#!/usr/bin/env python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import requests

extip = requests.get('http://canhazip.com').text
fromaddr = 'username@email.com'
toaddrs  = 'username@email.com'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddrs
msg['Subject'] = "Subject"

msg.attach(MIMEText(extip, 'plain'))

server = smtplib.SMTP('smtp.email.com',587)
server.ehlo()
server.starttls()
server.login(fromaddr, "password")
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()

