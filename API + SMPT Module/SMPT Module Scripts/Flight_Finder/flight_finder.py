# Code will be updated soon
import requests
import json

FLY_FROM = "HYD" #Change this field to IATA code of place you want to fly from
FLY_TO = "MEL" #Change this field to IATA code of place you want to fly 

def dt_formatter(dt):
    date = dt[0:10]
    time = dt[11:16]
    return f"{date} at {time}"

class FlightSearch:
    def __init__(self):
        self.API_KEY="" #Enter Your API Key Here
        self.url="https://api.tequila.kiwi.com/locations/query"

    def get_price(self):
        search_url = "https://api.tequila.kiwi.com/v2/search"
        header = { 
            "apikey": self.API_KEY,
            "Accept": "application/json"
        }
        parameter = {
            "fly_from": FLY_FROM,
            "fly_to": FLY_TO,
            "date_from": "05/02/2024",
            "date_to": "10/02/2024",
            "max_fly_duration": "18",
            "adults": "1",
            "selected_cabins": "M",
            # "adult_hold_bag": "2",
            # "adult_hand_bag": "1",
            "max_stopovers": "1",
            "curr": "INR",
        }
        response = requests.get(url=search_url, headers=header, params=parameter)
        temp = response.json()
        return temp
    
fs = FlightSearch()
data = fs.get_price()

with open("scrap.json", "w") as file:
    json.dump(data, file)

with open("airline_codes.json", "r") as file:
    airline_codes = json.load(file)

for j in range(10):
    price = data["data"][j]["price"]
    hand_bag_limit = data["data"][j]["baglimit"]["hand_weight"]
    luggage_limit = data["data"][j]["baglimit"]["hold_weight"]
    link = data["data"][j]["deep_link"]
    bagagge_price = data["data"][j]["bags_price"]['1']

    route = [data["data"][0]["route"][i] for i in range(len(data["data"][0]["route"]))]

    print(f"FLIGHT NUMBER : {j+1}\nFROM: HYD\nTO: MEL\nPRICE: {price}")
    print(f"HAND BAGGAGE LIMIT (IN KGS): {hand_bag_limit}")
    print(f"CHECK-IN BAGGAGE LIMIT (IN KGS): {luggage_limit}")

    for i in range(len(route)):
        print(f"Route {i+1}: ")
        fly_from_city = route[i]["cityFrom"]
        fly_from_city_code = route[i]["cityCodeFrom"]
        fly_to_city = route[i]["cityTo"]
        fly_to_city_code = route[i]["cityCodeTo"]
        print(f"FROM: {fly_from_city} ({fly_from_city_code}) | TO: {fly_to_city} ({fly_to_city_code})")
        airline_name = route[i]["airline"]
        for k in range(len(airline_codes)):
            if str(airline_name) == airline_codes[k]["Carrier Code"]:
                airline_name = airline_codes[k]["Airline"]

        print(f"AIRLINES: {airline_name}")
        local_departure_timings = dt_formatter(route[i]["local_departure"])
        print(f"LOCAL DEPARTURE TIMINGS: {local_departure_timings}")
        local_arrival_timings = dt_formatter(route[i]["local_arrival"])
        print(f"LOCAL ARRIVAL TIMINGS: {local_arrival_timings} \n")
    
    print(f"For more information, follow this link: {link}")
    
    print("_____________________________________________________")
    






