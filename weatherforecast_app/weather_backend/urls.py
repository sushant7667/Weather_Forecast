from django.urls import path
# from .views import weather_forecast, get_weather_forecast, receive_weather_forecast
from weather_backend import views

urlpatterns = [
    # Other URL patterns
    path('weather_forecast', views.weather_forecast,name="weather_forecast"),
    # path('home', views.home,name="home"),
    path('get_weather_forecast', views.get_weather_forecast,name="get_weather_forecast"),
    path('receive_weather_forecast', views.receive_weather_forecast,name="receive_weather_forecast"),
    path('get_weather_forecast_id/<int:id>', views.get_weather_forecast_id,name="get_weather_forecast_id"),
]