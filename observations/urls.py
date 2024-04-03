from django.urls import path

from observations.views import (Observations, ObservationDetail)

urlpatterns = [
    path('observations/', Observations.as_view()),
    path('observations/{id}/', ObservationDetail.as_view())
]