import smtplib
import schedule
import time

sender_email = "your_email@example.com
app_password = "Gmail_app_password"
# app_password = "This is not your normal gmail password, its different!"

receiver_email = "reciever_email@example.com"

def send_email():

    subject = "Daily Report"
    body = "Hello,\n\nThis is your automated email."

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message)


    print("Email sent")

# schedule automation
schedule.every().day.at("22:20").do(send_email)

print("Automation started...")

while True:
    schedule.run_pending()
    time.sleep(1)
