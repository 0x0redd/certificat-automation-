import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, body, filename):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    # Attaching the file
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)
    message.attach(part)

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

# List of files and corresponding recipients
files_recipients = {
    "file1.pdf": "recipient1@yahoo.com",
    "file2.pdf": "recipient2@yahoo.com",
    "file3.pdf": "recipient3@yahoo.com"
}

# Your email credentials
sender_email = "your_email@yahoo.com"
sender_password = "your_password"

# Common subject and body for all emails
subject = "Certificate Attached"
body = "Dear Correspondent,\n\nPlease find attached your certificate.\n\nRegards,\nYour Name"

# Send emails for each file
for file, recipient in files_recipients.items():
    send_email(sender_email, sender_password, recipient, subject, body, file)
    print(f"Email sent to {recipient} for {file}")
