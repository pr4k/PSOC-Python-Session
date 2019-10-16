#login to the perticular gmail and then allow to unsafe apps https://myaccount.google.com/lesssecureapps

import smtplib 
import config 

def send_mail(subject, msg):
    try:
        send_to_email = 'aji.yash13@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject:{}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, send_to_email, message)
        server.quit()
        print("Email Sent Successfully!")
    except:
        print("Email failed to send")


subject = "This is the Subject of my Test Email"
msg = "Hey this is a python generated test email and this is the body of my test email."
send_mail(subject, msg)


