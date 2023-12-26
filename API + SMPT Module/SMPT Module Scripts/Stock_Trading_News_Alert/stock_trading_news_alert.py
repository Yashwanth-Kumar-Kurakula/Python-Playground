import json
import os
from dotenv import load_dotenv
import requests

# Load environment variables from the .env file
load_dotenv(".env")

# Retrieve API keys from environment variables
alphavatage_api_key = os.getenv("ALPHAVANTAGE_API_KEY")
newsapi_key = os.getenv("NEWS_API_KEY")

# Constants for the stock data
STOCK = "TSLA"  # Change value to the desired stock symbol
COMPANY_NAME = "Tesla"  # Change the value to the company name of the stock

# Parameters for Alpha Vantage API
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alphavatage_api_key,
}

# Parameters for News API
news_parameters = {
    "apikey": newsapi_key,
    "q": COMPANY_NAME
}

# Fetch stock data from Alpha Vantage API
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()

# Save stock data to a JSON file
with open("stock_data.json", "w") as file:
    json.dump(data, file)

# Load stock data from the saved JSON file
with open("stock_data.json", "r") as file:
    data = json.load(file)

# Extract keys dynamically from stock data
all_keys = list(data["Time Series (Daily)"].keys())

# Get the dates for yesterday and the day before yesterday
yesterday_date = all_keys[0]
day_before_yesterday_date = all_keys[1]

# Extract low prices for yesterday and the day before yesterday
yesterday_low = float(data["Time Series (Daily)"][yesterday_date]["3. low"])
day_before_yesterday_low = float(data["Time Series (Daily)"][day_before_yesterday_date]["3. low"])

# Calculate percentage difference in low prices
percentage_difference = ((day_before_yesterday_low - yesterday_low) / ((yesterday_low + day_before_yesterday_low) / 2)) * 100

# Print the rounded percentage difference
print(f"Percentage Difference: {round(percentage_difference, 2)}%")

# Fetch news data from News API
news = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
news.raise_for_status()

# Parse news data
news_data = news.json()

# Save news data to a JSON file
with open("news_data.json", "w") as file2:
    json.dump(news_data, file2)

# Extract headline and description from the first news article
headline = news_data["articles"][0]["title"]
description = news_data["articles"][0]["description"]

# Print the headline and description
print(f"Headline: {headline}")
print(f"Brief: {description}")

# Optional: Use Twilio API to automate message
# (You can add the Twilio API integration code here if needed or automate using SMPT Module + Pythonanywhere
