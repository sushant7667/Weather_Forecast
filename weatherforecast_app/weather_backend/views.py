from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import views
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
import requests
from rest_framework.response import Response
import datetime
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
import pytz

@api_view(['POST'])
def weather_forecast(request):
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')
    detailing_type = request.POST.get('detailing_type')

    weather_forecast = Weather_Forecast.objects.filter(latitude=latitude, longitude=longitude, detailing_type=detailing_type).first()
    print("weather_forecast",weather_forecast)

    if weather_forecast:
        # Check the freshness
        freshness_threshold = datetime.timedelta(minutes=settings.WEATHER_DATA_FRESHNESS_THRESHOLD)
        current_time = timezone.now().astimezone(pytz.timezone('Asia/Kolkata'))
        print("current_time",current_time)
        time_difference = current_time - weather_forecast.timestamp
        print("time_difference",time_difference)

        if time_difference <= freshness_threshold:
            serializer = WeatherForecastSerializer(weather_forecast)
            response_data = {
                "data": serializer.data,
                "response": {
                    "n": 1,
                    "msg": "Try after 10 minutes",
                    "Status": "Success"
                }
            }
            return JsonResponse(response_data)

    # API key
    api_key = '211afa91c513f1c55ac6f3d2b1dca4a9'
    print("api_key",api_key)
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&exclude=current,minutely,daily&appid={api_key}'

    print("API URL:", api_url) 

    response = requests.get(api_url)
    print("response",response)
    print("response content:", response.content)
    if response.status_code == 200:
        data = response.json()

        if not weather_forecast:
            weather_forecast = Weather_Forecast(latitude=latitude, longitude=longitude, detailing_type=detailing_type)

        # Update  forecast object
        weather_forecast.field1 = data.get('field1')
        weather_forecast.field2 = data.get('field2')

        # timestamp to the India timezone
        india_tz = pytz.timezone('Asia/Kolkata')
        timestamp = timezone.now().astimezone(india_tz)
        weather_forecast.timestamp = timestamp

        weather_forecast.save()
        serializer = WeatherForecastSerializer(weather_forecast)
        response_data = {
            "data": serializer.data,
            "response": {
                "n": 1,
                "msg": "Data has been stored successfully",
                "Status": "Success"
            }
        }
        return JsonResponse(response_data)
            
    response_data = {
        "data": {},
        "response": {
            "n": 0,
            "msg": "Error fetching weather data",
            "Status": "Failed"
        }
    }
    return JsonResponse(response_data)              


@api_view(['GET'])
def get_weather_forecast(request):
    weather_forecasts = Weather_Forecast.objects.all().order_by('id')
    serializer = WeatherForecastSerializer(weather_forecasts, many=True)

    if serializer.data:
        response_data = {
            "data": serializer.data,
            "response": {
                "n": 1,
                "msg": "Data found successfully",
                "Status": "Success"
            }
        }
        return Response(response_data)
    else:
        response_data = {
            "data": {},
            "response": {
                "n": 0,
                "msg": "No data found",
                "Status": "Failed"
            }
        }
        return Response(response_data)

@api_view(['GET'])
def receive_weather_forecast(request):
    weather_forecasts = Weather_Forecast.objects.all()
    serializer = WeatherForecastSerializer(weather_forecasts, many=True)

    if serializer.data:
        response_data = {
            "data": serializer.data,
            "response": {
                "n": len(weather_forecasts),
                "msg": "Weather forecasts retrieved successfully",
                "Status": "Success"
            }
        }
        return JsonResponse(response_data)
    else:
        response_data = {
            "data": {},
            "response": {
                "n": 0,
                "msg": "No data found",
                "Status": "Failed"
            }
        }
        return JsonResponse(response_data)

@api_view(['GET'])
def get_weather_forecast_id(request,id):
    weather_forecasts=Weather_Forecast.objects.filter(id=id,isactive=True).first()
    print ("weather_forecasts",weather_forecasts)
    if weather_forecasts is not None:
        serializer=WeatherForecastSerializer(weather_forecasts)
        Response_ = {
            "data":serializer.data,
            "response":{
                "n":1,
                "msg":"Data has been found successfully",
                "Status":"Success"

            }
        }
        return Response(Response_)
    else:
        Response_ = {
            "data":{},
            "response":{
                "n":0,
                "msg":"No data found",
                "Status":"Failed"

            }
        }
        return Response(Response_)