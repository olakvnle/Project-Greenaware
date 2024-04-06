from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (Country, City)
from weathers.serializers import CountrySerializer, BulkCountrySerializer, CitySerializer


class Countries(APIView):
    def get(self, request, format=None):
        """Fetch all countries from the database"""
        countries = Country.objects.all()
        """Serialize the queryset using the serializer"""
        serializer = CountrySerializer(countries, many=True)
        """Return response with serialized data and status code"""
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=CountrySerializer,
        responses={status.HTTP_201_CREATED: CountrySerializer},
    )
    def post(self, request, format=None):
        """Create a new countries"""
        """Serialize the queryset using the serializer"""
        serializer = CountrySerializer(data=request.data)
        """Check whether the request data is valid"""
        if serializer.is_valid():
            """Save the serialized data"""
            serializer.save()
            # countries = [Country(**data) for data in serializer.validated_data]
            # Country.objects.bulk_create(countries)
            """return response with serialized data and status code"""
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Cities(APIView):
    def get(self, request, format=None):
        """Fetch all cities from the database"""
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        """Return response with serialized data and status code"""
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        """Create a new cities"""
        serializer = CitySerializer(data=request.data)
        """Check whether the request data is valid"""
        if serializer.is_valid():
            """Save the serialized data"""
            serializer.save()
            """return response with serialized data and status code"""
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Location(APIView):
    # permission_classes = [permissions.AllowAny]

    def get(self, request):
        content = {'message': 'Hello World!'}
        return Response(content)
