from rest_framework import serializers
from .models import Country, City


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']


class BulkCountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']
