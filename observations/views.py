from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Observation
from .serializers import ObservationSerializer
from django.shortcuts import get_object_or_404

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
        serializer = ObservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ObservationDetail(APIView):
#     @swagger_auto_schema(
#         responses={status.HTTP_200_OK: ObservationSerializer()}
#     )
#     def get(self, request, pk, format=None):
#         """Retrieve a specific observation by primary key"""
#         observation = self.get_object(pk)
#         if observation is not None:
#             serializer = ObservationSerializer(observation)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response({"error": "Observation not found"}, status=status.HTTP_404_NOT_FOUND)

#     @swagger_auto_schema(
#         request_body=ObservationSerializer,
#         responses={status.HTTP_200_OK: ObservationSerializer()}
#     )
#     def put(self, request, pk, format=None):
#         """Update an existing observation"""
#         observation = self.get_object(pk)
#         if observation is not None:
#             serializer = ObservationSerializer(observation, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"error": "Observation not found"}, status=status.HTTP_404_NOT_FOUND)

#     @swagger_auto_schema(
#         responses={status.HTTP_204_NO_CONTENT: "Observation deleted successfully"}
#     )
#     def delete(self, request, pk, format=None):
#         """Delete an existing observation"""
#         observation = self.get_object(pk)
#         if observation is not None:
#             observation.delete()
#             return Response({"message": "Observation deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#         return Response({"error": "Observation not found"}, status=status.HTTP_404_NOT_FOUND)

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