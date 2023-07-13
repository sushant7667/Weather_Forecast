from django.shortcuts import render,redirect
from . import views
from rest_framework.decorators import api_view
from .models import *
import requests
from rest_framework.response import Response
from django.contrib import messages
from weather_backend.models import Weather_Forecast

# urls 
addweatherurl='http://127.0.0.1:8000/weather_backend/weather_forecast'
getweatherurl='http://127.0.0.1:8000/weather_backend/get_weather_forecast'
getweatheridurl='http://127.0.0.1:8000/weather_backend/get_weather_forecast_id/'

def front_weather_forecast(request):
    if request.method == 'POST':
        data={}
        data['latitude']=request.POST.get('latitude')
        data['longitude']=request.POST.get('longitude')
        data['detailing_type']=request.POST.get('detailing_type')
        print("data",data)

        responseurl=requests.post(addweatherurl,data=data)
        print('responseurl',responseurl)
        result = responseurl.json()

        if result['response']['n'] == 1:
                messages.success(request, result['response']['msg'])
                return redirect('weather_frontend:front_get_weather_forecast_id',id=result['data']['id'])
        else:
                messages.error(request, result['response']['msg'])
                return redirect('weather_frontend:front_get_weather_forecast_id', id=result['data']['id']) 

    return render(request, 'add_weather_forecast.html') 


def front_get_weather_forecast(request):
        response = requests.get(getweatherurl)
        geodata = response.json()
        return render(request,'get_allweather.html',{'data':geodata['data']})

def front_get_weather_forecast_id(request,id):
        if request.method == "GET":
                GetData = getweatheridurl + str(id)
                response=requests.get(GetData)
                geodata = response.json()
                return render(request,'get_weather_forecast.html',{'data':geodata['data']})