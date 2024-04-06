from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Observation

class ObservationTests(APITestCase):
    def setUp(self):
        self.observation_data = {
            "date": "2023-12-31",
            "time": "12:00:00",
            "timeZoneOffset": "UTC-10:00",
            "coordinates": "5.42,87.32",
            "temperatureLandSurface": 8.0,
            "temperatureSeaSurface": 10.0,
            "humidity": 5.0,
            "windSpeed": 5.0, 
            "windDirection": "23.43,43.875",
            "precipitation": 35.0,
            "haze": 29.0,
            "notes": "The weather is weird",
        }

    def test_create_observation(self):
        url = reverse('observations-list')
        response = self.client.post(url, self.observation_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Observation.objects.count(), 1)
        self.assertEqual(Observation.objects.get().date, "2023-12-31")

    def test_retrieve_observation(self):
        observation = Observation.objects.create(**self.observation_data)
        url = reverse('observations-detail', args=[observation.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['date'], "2023-12-31")

    def test_update_observation(self):
        observation = Observation.objects.create(**self.observation_data)
        url = reverse('observations-detail', args=[observation.id])
        updated_data = {
            "date": "2024-01-01",
            "time": "13:00:00",
            "coordinates": "10.42,20.32"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['date'], "2024-01-01")

    def test_delete_observation(self):
        observation = Observation.objects.create(**self.observation_data)
        url = reverse('observations-detail', args=[observation.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Observation.objects.count(), 0)
