from django.urls import path,include
from django.contrib import admin
from weather_frontend import views

urlpatterns = [
    path('front_weather_forecast', views.front_weather_forecast,name="front_weather_forecast"),
    path('front_get_weather_forecast', views.front_get_weather_forecast,name="front_get_weather_forecast"),
    path('front_get_weather_forecast_id/<int:id>', views.front_get_weather_forecast_id,name="front_get_weather_forecast_id"),
]