import datetime as dt
import random
import math
import smtplib
from email.mime.text import MIMEText

with open("quotes.txt") as file:
    quotes = file.readlines()

quote = random.choice(quotes)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = dt.datetime.now().weekday()


def remaining_weeks():
    now = dt.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    date = dt.date(year, month, day)
    target = dt.date(2029, 9, 6)
    delta_weeks = (target - date).days/7
    return math.floor(delta_weeks)


def send_email(week, quote):
    port = 465
    password = "SENDER_PASSWORD"
    sender_email = "SENDER_EMAIL"
    receiver_email = "TARGET_EMAIL"
    message = MIMEText(f"{quote} \n You have {week} weeks to your ...th birthday! ")
    message['Subject'] = f"Daily Motivation - {days[day]}"
    message['From'] = sender_email
    message['To'] = receiver_email

    server = smtplib.SMTP_SSL("smtp.gmail.com", port)
    server.login(sender_email, password)
    server.sendmail(sender_email, [receiver_email], message.as_string())
    server.quit()


if day < 7:
    print("Sending..")
    send_email(remaining_weeks(), quote)
    print("Done")
