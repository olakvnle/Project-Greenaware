from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class Location(APIView):
    # permission_classes = [permissions.AllowAny]

    def get(self, request):
        content = {'message': 'Hello World!'}
        return Response(content)
