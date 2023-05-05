import requests
import datetime as dt

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "37790a5dbd1c0bfbb6e4f9f5881465e5"
CITY ="kolbotn"

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
wind_speed = response['wind']['speed']


print(f"Temperatur : {CITY}: {temp_celsius: .2f} C")
print(f"Vindhastiighet: {CITY}: {wind_speed:}M/S")
print(f"luftfuktighet: {CITY}: {humidity}%")
print(f"Generelt vær: {CITY}: {description}")

