import smtplib
import random
import datetime as dt

def send_motivational_email():
    """
    Sends a motivational email with a random quote and a Python tip of the day.

    Make sure to replace placeholders such as "Replace with your email" and "Replace with To Address".
    """

    # Replace with your email and password
    my_email = "Replace with your email"
    password = "Replace with your password"

    # Get the current date and time
    now = dt.datetime.now()

    # Read quotes from the quotes.txt file
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()

    # Read Python tips from the python_tips.txt file
    with open("python_tips.txt", "r") as u:
        python_tips = u.read()

    # Choose a random quote
    quote = random.choice(quotes)

    # Split Python tips into a list
    tips = python_tips.split("\n\n")

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Start a secure TLS connection
        connection.starttls()

        # Log in to the email account
        connection.login(user=my_email, password=password)

        # Send the email
        connection.sendmail(from_addr=my_email,
                            to_addrs="Replace with To Address",
                            msg=f"Subject:Daily Motivation by DelusionalDeveloper \n\n{quote} \n Tip of the day: {tips[random.randint(0, 39)]}")

# Call the function to send the motivational email
send_motivational_email()
