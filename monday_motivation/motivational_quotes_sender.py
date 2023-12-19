import smtplib
import random
import datetime as dt

my_email = "Enter your email here"
password = "Enter your password here"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", "r") as f:
        x = f.readlines()
    
    quote = random.choice(x)
    with smtplib.SMTP("Enter your smtp here") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="Enter the email you want to send the mail", 
                            msg=f"Subject:Motivational Quotes test \n\n{quote}")
