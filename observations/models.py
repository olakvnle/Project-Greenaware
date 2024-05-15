from django.db import models

from django.db import models
from django.conf import settings

class Observation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    timeZoneOffset = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    temperatureLandSurface = models.DecimalField(max_digits=5, decimal_places=2)
    temperatureSeaSurface = models.DecimalField(max_digits=5, decimal_places=2)
    coordinate_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    coordinate_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)
    windSpeed = models.DecimalField(max_digits=5, decimal_places=2)
    windDirection = models.CharField(max_length=50)
    precipitation = models.DecimalField(max_digits=5, decimal_places=2)
    haze = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField()

    def __str__(self):
        return f"Observation - {self.date} {self.time}"


class ApiKeys(models.Model):
    user_id = models.IntegerField()
    api_key = models.CharField(max_length=100)
    expires_at = models.DateTimeField()
    rate_limit = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_valid(self):
        """
        Check if the API key is valid (not expired).
        """
        return self.expires_at > timezone.now()

    def has_expired(self):
        """
        Check if the API key has expired.
        """
        return not self.is_valid()
