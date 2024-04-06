from django.db import models

# Create your models here.
from django.db import models

class Observation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    timeZoneOffset = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    temperatureLandSurface = models.DecimalField(max_digits=5, decimal_places=2)
    temperatureSeaSurface = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    windSpeed = models.DecimalField(max_digits=5, decimal_places=2)
    windDirection = models.CharField(max_length=50)
    precipitation = models.DecimalField(max_digits=5, decimal_places=2)
    haze = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField()

    def __str__(self):
        return f"Observation - {self.date} {self.time}"