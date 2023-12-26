import json
import os
from dotenv import load_dotenv
import requests

load_dotenv(".env")
alphavatage_api_key = os.getenv("ALPHAVANTAGE_API_KEY")
newsapi_key = os.getenv("NEWS_API_KEY")

STOCK = "TSLA" # Change value to desired Stock
COMPANY_NAME = "Tesla" # Change the value to the company name of the stock

parameters = {
"function": "TIME_SERIES_DAILY",
"symbol": STOCK,
"apikey": alphavatage_api_key,
}

news_parameters = {
    "apikey": newsapi_key,
    "q": COMPANY_NAME
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()

with open("stock_data.json", "w") as file:
    json.dump(data, file)

with open("stock_data.json", "r") as file:
    data = json.load(file)

all_keys = list(data["Time Series (Daily)"].keys())

yesterday_date = all_keys[0]
day_before_yesterday_date = all_keys[1]

yesterday_low = float(data["Time Series (Daily)"][yesterday_date]["3. low"])
day_before_yesterday_low = float(data["Time Series (Daily)"][day_before_yesterday_date]["3. low"])

percentage_difference = ((day_before_yesterday_low - yesterday_low) / ((yesterday_low + day_before_yesterday_low) / 2)) * 100
print(round(percentage_difference, 2))

news = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
news.raise_for_status()

news_data = news.json()
with open("news_data.json", "w") as file2:
    json.dump(news_data, file2)

Headline = news_data["articles"][0]["title"]
description = news_data["articles"][0]["description"]

print(f"Headline: {Headline}")
print(f"Brief: {description}")

#Optional: Use Twilio API to automate message