import smtplib

SENDER_EMAIL = 'email'
SENDER_PASSWORD = 'password'

def send_email(receiver_email,subject,body):
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP('mail.email.net', 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)
        print(message)

'''
To execute this code, the code itself needs to be changed. Please, be aware of security concerns and make sure you don't share your password or other relevant data.
user, Password, host (SMTP host), port (SMPT port) and e-mail should be adapted according to your prefered e-mail service.
Once the code is changed, please also adapt and uncomment the line below.
'''

# send_email('receiver','subject','message'):