from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from datetime import datetime, timedelta
import datetime


def index(request):
    return HttpResponse("Hello world!")


def home(request):
    return render(request, "home.html",{})


def getweather(request):
    lat = '39.74'
    long = '-104.98'
    appid = 'a86a7958a4911de6e45a564ecdd933ac'
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&units=imperial&appid={appid}"

    payload = {}
    headers = {}

    weather = requests.request("GET", url, headers=headers, data=payload)
    weather = json.loads(weather.text)

    url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={long}&limit=1&appid={appid}"

    payload = {}
    headers = {}

    location = requests.request("GET", url, headers=headers, data=payload)
    location = json.loads(location.text)
    conditons = weather['weather'][0]
    sunrise = weather['sys']['sunrise']
    sunrise = datetime.datetime.fromtimestamp(sunrise) - timedelta(hours=6, minutes=00)
    sunrise = sunrise.strftime("%I:%M %p")
    sunset = weather['sys']['sunset']
    sunset = datetime.datetime.fromtimestamp(sunset) - timedelta(hours=6, minutes=00)
    sunset = sunset.strftime("%I:%M %p")
    suntimes = {
        "sunrise": sunrise,
        "sunset": sunset,
    }

    context = {
        "location": location[0],
        "weather": weather,
        "conditions": conditons,
        "suntimes": suntimes,
    }

    return render(request, "home.html", context)


