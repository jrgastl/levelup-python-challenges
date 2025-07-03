'''
Author Note:
With this exercise I could understand and learn about smtplib module by creating a smtplib object and sending a message with it. I had to format the text with MIME text method of the
email.mime.text module to be able to use my e-mail server to send the message, since it required the 'From' field correctly filled.
'''

import smtplib
from email.mime.text import MIMEText

def send_email(receiver,subject,message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'e-mail'
    msg['To'] = receiver
    print(msg)
    
    user = 'e-mail'
    password ='password'
    server = smtplib.SMTP(host='mail.email.net', port=587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()