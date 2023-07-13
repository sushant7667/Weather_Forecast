from rest_framework import serializers
from .models import *
from django.utils import timezone
import pytz

class WeatherForecastSerializer(serializers.ModelSerializer):
    # ... existing code ...
    class Meta:
        model = Weather_Forecast
        fields = '__all__'

    def to_representation(self, instance):
        # india_tz = pytz.timezone('Asia/Kolkata')
        # timestamp = instance.timestamp.astimezone(india_tz)
        # representation = super().to_representation(instance)
        # representation['timestamp'] = timestamp.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        # return representation
        india_tz = pytz.timezone('Asia/Kolkata')
        timestamp = timezone.localtime(instance.timestamp, india_tz)
        representation = super().to_representation(instance)
        representation['timestamp'] = timestamp.isoformat()
        return representation