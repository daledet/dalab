import requests

url = "http://api.openweathermap.org/data/2.5/weather?id=3137115&"
api = "appid=4fbcfd9147ff6df0e3ee3de039a4e70c&units=metric"

response = requests.get(url, api)
data = response.json()
print(data)
