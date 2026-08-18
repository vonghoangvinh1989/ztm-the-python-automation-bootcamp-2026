import smtplib
import app_password

sender_email = 'vonghoangvinh1989business@gmail.com'
password = app_password.password

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls() # sending the email, the email will be encrypted, connection will be secured
    connection.login(user=sender_email, password=password)

    connection.sendmail(
        from_addr=sender_email,
        to_addrs=sender_email,
        msg='Subject:Hello...\n\n...World!'
    )