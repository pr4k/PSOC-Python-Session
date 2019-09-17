import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = 'coderaji13@gmail.com'
password = ''
send_to_email = 'coderaji13@gmail.com'
subject = 'Test Email Using Python'
message = 'This is my message'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()