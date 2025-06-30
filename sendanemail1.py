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