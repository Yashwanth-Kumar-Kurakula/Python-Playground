import smtplib
import random
import datetime as dt

my_email = "Replace with your email"
password = "Replace with your password"

now = dt.datetime.now()

with open("quotes.txt", "r") as f:
    x = f.readlines()

with open("python_tips.txt", "r") as u:
    y = u.read()

quote = random.choice(x)
tips = y.split("\n\n")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="Replace with To Address",
                        msg=f"Subject:Daily Motivation by DelusionalDeveloper \n\n{quote} \n Tip of the day: {random.randint(0,99)}")


