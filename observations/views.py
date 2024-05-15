from django.shortcuts import render
from rest_framework import permissions

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Observation
from .serializers import ObservationSerializer, APIKeySerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from .what3words import what3words_instance
from .models import ApiKeys


def has_permission(request):
    # Check if the user has an API key
    api_key = request.META.get('api_key')  # Assuming you pass the API key in the request headers
    if api_key:
        # Check if the API key exists in the APIKey table
        try:
            api_key_instance = ApiKeys.objects.get(api_key=api_key)
            # If the API key exists, allow access without authentication
            print(api_key_instance)
            return True
        except ApiKeys.DoesNotExist:
            # If the API key does not exist, deny access
            return False
    else:
        # If no API key is provided, deny access
        return False


class ObservationsWithApiKey(APIView):
    authentication_classes = []

    def get(self, request, format=None):
        # Override authentication_classes for GET method
        api_key = has_permission(request);
        print(api_key)
        """Fetch all observations from the database"""
        observations = Observation.objects.all()
        serializer = ObservationSerializer(observations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Observations(APIView):
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: ObservationSerializer(many=True)}
    )
    def get(self, request, format=None):

        """Fetch all observations from the database"""
        observations = Observation.objects.all()
        serializer = ObservationSerializer(observations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=ObservationSerializer,
        responses={status.HTTP_201_CREATED: ObservationSerializer()}
    )
    def post(self, request, format=None):
        """Create a new observation"""
        if isinstance(request.data, list):
            data = request.data[0]  # Assuming the user ID is in the first item
        else:
            data = request.data
        data['user'] = request.user.id

        what3words = data.pop('location')

        what3words_data, error_message = what3words_instance.process_what3words_response(what3words)
        if what3words_data is None:
            return Response(error_message)

        coordinate_data = what3words_instance.get_coordinates(what3words_data)

        # Extract latitude and longitude from coordinate_data
        latitude = coordinate_data.get('coordinate_latitude')
        longitude = coordinate_data.get('coordinate_longitude')

        # Add latitude and longitude to the data
        data['coordinate_latitude'] = latitude
        data['coordinate_longitude'] = longitude
        data['location'] = what3words

        # Pass the modified data to the serializer
        serializer = ObservationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObservationsBulk(APIView):
    @swagger_auto_schema(
        request_body=ObservationSerializer(many=True),
        responses={status.HTTP_201_CREATED: ObservationSerializer(many=True)}
    )
    def post(self, request, format=None):
        """Create new observations"""
        # if isinstance(request.data, list):
        #     data = request.data[0]  # Assuming the user ID is in the first item
        # else:
        #     data = request.data
        # data['user'] = request.user.id
        for observation in request.data:
            observation['user'] = request.user.id

        serializer = ObservationSerializer(data=request.data, many=True)
        if serializer.is_valid():
            # serializer.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserObservations(APIView):
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: ObservationSerializer(many=True)}
    )
    def get(self, request, user_id, format=None):
        """Get observations by user"""
        observations = Observation.objects.filter(user_id=user_id)
        serializer = ObservationSerializer(observations, many=True)
        return Response(serializer.data)


class ObservationDetail(APIView):
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: ObservationSerializer()}
    )
    def get(self, request, pk, format=None):
        """Retrieve a specific observation by primary key"""
        observation = get_object_or_404(Observation, pk=pk)
        serializer = ObservationSerializer(observation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=ObservationSerializer,
        responses={status.HTTP_200_OK: ObservationSerializer()}
    )
    def put(self, request, pk, format=None):
        """Update an existing observation"""
        observation = get_object_or_404(Observation, pk=pk)
        serializer = ObservationSerializer(observation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={status.HTTP_204_NO_CONTENT: "Observation deleted successfully"}
    )
    def delete(self, request, pk, format=None):
        """Delete an existing observation"""
        observation = get_object_or_404(Observation, pk=pk)
        observation.delete()
        return Response({"message": "Observation deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class GenerateAPIKeys(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = ()

    def post(self, request):
        data = request.data
        serializer = APIKeySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
