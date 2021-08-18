import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()
my_email = 'kanha123app@gmail.com'
my_password = "1234ishaan"
with open("quotes.txt", mode="r") as quotes_file:
    quotes = quotes_file.readlines()

if day_of_week == 0:
    quote_today = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="agrawalishaan115@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote_today}"
        )
