from django.shortcuts import render
import requests
import json

# Create your views here.

def home(request):
    url = "http://api.aladhan.com/v1/calendarByCity/2023/5"

    querystring = {"country":" South Korea","city":"Seoul","method":"1","school":"1"}
    response = requests.get(url, params=querystring)
    data = response.json()

    return render(request,'prayer/home.html',{"response":response.json()})
