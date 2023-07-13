from django.db import models

# Create your models here.

class Weather_Forecast(models.Model):
    
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    Choices=('Minute','Minute'),('Hourly','Hourly'),('Daily','Daily')
    detailing_type = models.CharField(choices=Choices,max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=True)
