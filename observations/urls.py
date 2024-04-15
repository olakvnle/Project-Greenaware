from django.urls import path

from observations.views import (Observations, ObservationsBulk, UserObservations, ObservationDetail)

urlpatterns = [
    path('observations/', Observations.as_view()),
    path('observations/<int:pk>/', ObservationDetail.as_view()),
    path('observations/user/<user_id>', UserObservations.as_view()),
    path('observations/bulk/', ObservationsBulk.as_view())
]