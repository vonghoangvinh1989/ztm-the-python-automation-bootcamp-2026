# import libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import app_password
from datetime import date

# get current date
today = date.today().strftime("%Y-%m-%d")

# create MIME object
sender_email = "vonghoangvinh1989business@gmail.com"

email_subject = f"Status Report for {today}"

# import emails from file
with open("project_emails.txt", "r") as file:
    emails = [email.strip() for email in file.readlines()]

emails_string = ", ".join(emails)

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = emails_string
message['Subject'] = email_subject
password = app_password.password

# import data from text file
with open("customer_complaints.txt", "rb") as attachment:
    complaints = attachment.readlines()
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="customer_complaints.txt"')

email_body = f"There are {len(complaints) - 1} complaints in today's file."
message.attach(MIMEText(email_body, 'plain'))
message.attach(part)

message_string = message.as_string()

# send email with smtplib
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls() # sending the email, the email will be encrypted, connection will be secured
    connection.login(user=sender_email, password=password)

    connection.sendmail(
        from_addr=sender_email,
        to_addrs=emails,
        msg=message_string
    )