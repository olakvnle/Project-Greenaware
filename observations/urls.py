from django.urls import path

from observations.views import (Observations, ObservationDetail)

urlpatterns = [
    path('observations/', Observations.as_view()),
    path('observations/<int:pk>/', ObservationDetail.as_view())
]