#!/usr/bin/env python3

import requests
import json

# Simple function to request and return parsed JSON
def get_json(url):
    content = requests.get(url).text
    return json.loads(content)

'''
Getting location info from current IP
'''
location_api = "http://ip-api.com/json/"
location_data = get_json(location_api)

city = location_data["city"]
region = location_data["regionName"]
lat = location_data["lat"]
lon = location_data["lon"]

'''
Getting weather for location from above function
'''
weather_api_key="ee24366fedab935ab8870a577fe1a060"
weather_api_url="https://api.darksky.net/forecast/{}/{},{}?units=si".format(weather_api_key, lat, lon)

weather_data = get_json(weather_api_url)

summary = weather_data["daily"]["summary"]
rain_probability = weather_data["daily"]["data"][0]["precipProbability"]
temp_high = weather_data["daily"]["data"][0]["temperatureHigh"]
temp_low = weather_data["daily"]["data"][0]["temperatureLow"]


'''
Pretty Printing all the weather data
'''
print("Weather info for {}, {}:".format(city, region),
    '-'*40,
    "Description: {}".format(summary), 
    "Rain Probability: {}%".format(rain_probability*100),
    "TemperatureHigh: {} °C".format(temp_high),
    "TemperatureLow: {} °C".format(temp_low),
    sep="\n"
)