from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def getweather():
    lat = '33.4484367'
    long = '-112.074141'
    appid = ''
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&units=imperial&appid={appid}"

    weather = requests.request("GET", url)
    weather = json.loads(weather.text)

    print (type(weather))

    url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={long}&limit=1&appid={appid}"

    location = requests.request("GET", url)
    location = json.loads(location.text)

    print (type(location[0]))

    context = {
        "location": json.loads(location.text),
        "weather": json.loads(weather.text),
    }

    return context

print(getweather())