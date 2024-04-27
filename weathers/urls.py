from django.urls import path
from .views import (Location, Countries,Cities)

urlpatterns = [
    path('countries/', Countries.as_view(), name='country-list'),
    path('cities/', Cities.as_view(), name='city-list'),
    path('locations/', Location.as_view())
]