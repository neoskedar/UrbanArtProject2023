from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from datetime import datetime, timedelta
import datetime
from . import forms
from .forms import GetLocation


def index(request):
    return HttpResponse("Hello world!")


def home(request):
    form = forms.GetLocation()
    # Check to see if we are getting a POST request back
    if request.method == "POST":
        # if post method = True
        form = forms.GetLocation(request.POST)
        # Then we check to see if the form is valid (this is an automatic  validation by Django)
        if form.is_valid():
            # if form.is_valid == True then do something
            print("Form validation successful! See console for information:")
            print("Location: " + form.cleaned_data['location'])
            return getlocation(request, form.cleaned_data['location'])
    return render(request, 'home.html', {'form': form})


def getweather(request, lat, long):
    # lat = '55.7504461'
    # long = '37.6174943'
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
    offset = weather['timezone'] / 60 / 60
    print(offset)
    sunrise = weather['sys']['sunrise']
    sunset = weather['sys']['sunset']
    if offset < 0:
        offset = abs(offset)
        sunrise = datetime.datetime.fromtimestamp(sunrise) - timedelta(hours=offset, minutes=00)
        sunset = datetime.datetime.fromtimestamp(sunset) - timedelta(hours=offset, minutes=00)
    else:
        offset = abs(offset)
        sunrise = datetime.datetime.fromtimestamp(sunrise) + timedelta(hours=offset, minutes=00)
        sunset = datetime.datetime.fromtimestamp(sunset) + timedelta(hours=offset, minutes=00)
    sunrise = sunrise.strftime("%I:%M %p")
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

    return render(request, "weather.html", context)


def getlocation(request, city):
    appid = 'a86a7958a4911de6e45a564ecdd933ac'

    url = f"http://api.openweathermap.org/geo/1.0/direct?limit=5&q={city}&appid={appid}"

    payload = {}
    headers = {}

    geo = requests.request("GET", url, headers=headers, data=payload)
    geo = json.loads(geo.text)

    context = {
        "geo": geo,
    }

    return render(request, "location.html", context)
