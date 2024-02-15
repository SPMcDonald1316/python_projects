import requests
import config
from pprint import pprint

city = input("Enter a city: ")

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.api_key}'

weather_data = requests.get(url)
