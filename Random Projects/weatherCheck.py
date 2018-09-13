"""
Project From Automate The Boring Stuff Chapter 14
Project: Fetching Current Weather Data
Github: MattDWe
Prints current weather for a location
"""

import json, requests, sys

#Compute location from command line arguments.
if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()
location = " ".join(sys.argv[1:])

#Download the JSON data from OpenWeatherMap.orgs API
url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3" % (location)
response = requests.get(url)
response.raise_for_status()

#Load JSON data into a Python variable.
weatherData = json.loads(response.text)
#Print weather descriptions.
w = weatherData["list"]
print("Current Weather in %s:" % (location))
print(w[0]["weather"][0]["main"], "-", w[0]["weather"][0]["description"])
print()
