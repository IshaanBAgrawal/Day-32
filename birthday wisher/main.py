import datetime as dt
import random
import smtplib
import pandas

now = dt.datetime.now()
today_date = now.day
today_month = now.month

data = pandas.read_csv("birthdays.csv")
dates = data.values.tolist()

my_email = "kanha123app@gmail.com"
my_password = "1234ishaan"

for members in dates:
    if today_date == int(members[4]) and today_month == int(members[3]):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            letter_choice = random.randint(1, 3)
            with open(f"letter_templates/letter_{letter_choice}.txt") as letter_chosen:
                letter = letter_chosen.read()
                new_letter = letter.replace("[NAME]", members[0])
            connection.sendmail(
                from_addr=my_email,
                to_addrs=members[1],
                msg=f"Subject:HAPPY BIRTHDAY!\n\n{new_letter}"
            )
