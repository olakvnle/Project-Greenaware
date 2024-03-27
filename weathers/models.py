from django.db import models
from django.conf import settings


# Table for name of countries
class Country(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def create_bulk(cls, data_list):
        countries = [cls(name=data['name']) for data in data_list]
        return cls.objects.bulk_create(countries)


class City(models.Model):
    name = models.CharField(unique=True,max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Coordinates(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Temperature(models.Model):
    land_surface = models.DecimalField(max_digits=5, decimal_places=2)
    sea_surface = models.DecimalField(max_digits=5, decimal_places=2)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Wind(models.Model):
    speed = models.DecimalField(max_digits=5, decimal_places=2)
    direction = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class WeatherData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    time_zone_offset = models.CharField(max_length=100)
    coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE)
    temperature = models.ForeignKey(Temperature, on_delete=models.CASCADE)
    wind = models.ForeignKey(Wind, on_delete=models.CASCADE)
    precipitation = models.DecimalField(max_digits=5, decimal_places=2)
    haze = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField()

    def __str__(self):
        return f"Weather data for {self.city} on {self.date} at {self.time}"
