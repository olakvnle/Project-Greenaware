from django.urls import path
from .views import Location

urlpatterns = [
    path('locations/', Location.as_view())
]