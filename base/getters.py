import requests
import json

import os
import datetime
os.system('clear')


url_stavanger = "http://api.openweathermap.org/data/2.5/weather?id=3137115&"
url_bergen = "http://api.openweathermap.org/data/2.5/weather?id=3161733&"

response_stavanger = requests.get(
    url_stavanger, "appid=4fbcfd9147ff6df0e3ee3de039a4e70c&units=metric")

response_bergen = requests.get(
    url_bergen, "appid=4fbcfd9147ff6df0e3ee3de039a4e70c&units=metric")

data_stavanger = response_stavanger.json()
print(data_stavanger)
data_bergen = response_bergen.json()

wind_speed_stavanger = response_stavanger.json()['wind']['speed']
print(wind_speed_stavanger)
wind_degree_stavanger = response_stavanger.json()['wind']['deg']
turbine_location_stavanger = response_stavanger.json()['name']

wind_speed_bergen = response_bergen.json()['wind']['speed']
wind_degree_bergen = response_bergen.json()['wind']['deg']
turbine_location_bergen = response_bergen.json()['name']

sunrise = response_stavanger.json()['sys']['sunrise']

ts_epoch = sunrise
ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%H:%M:%S')
