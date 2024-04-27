from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from observation.models import Observation
from .serializers import ObservationSerializer
from datetime import date, time

User = get_user_model()

class ObservationViewTests(TestCase):
    def setUp(self):
        # Setting up a user and client for API interaction
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Creating an Observation instance to use in tests
        self.observation = Observation.objects.create(
            user=self.user,
            date=date.today(),
            time=time(12, 0),
            timeZoneOffset="+00:00",
            location="Test Location",
            temperatureLandSurface=25.5,
            temperatureSeaSurface=26.5,
            humidity=75.00,
            windSpeed=10.5,
            windDirection="NE",
            precipitation=2.5,
            haze=10.2,
            notes="Sample observation notes."
        )

    def test_get_observations(self):
        response = self.client.get('/observations/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assumes only one observation in the database

    def test_post_observations(self):
        data = {
            'user': self.user.id,
            'date': '2023-04-01',
            'time': '15:00:00',
            'timeZoneOffset': "+00:00",
            'location': "New Location",
            'temperatureLandSurface': 30.0,
            'temperatureSeaSurface': 28.0,
            'humidity': 80.0,
            'windSpeed': 15.0,
            'windDirection': "NW",
            'precipitation': 5.0,
            'haze': 12.0,
            'notes': "Additional observation notes."
        }
        response = self.client.post('/observations/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_observation_detail(self):
        url = f'/observations/{self.observation.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.observation.id)

    def test_put_observation_detail(self):
        url = f'/observations/{self.observation.id}/'
        updated_data = ObservationSerializer(self.observation).data
        updated_data['temperatureLandSurface'] = 22.5
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['temperatureLandSurface'], 22.5)

    def test_delete_observation_detail(self):
        url = f'/observations/{self.observation.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Observation.objects.filter(id=self.observation.id).exists())

    def test_user_observations(self):
        url = f'/observations/user/{self.user.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assumes this user has one observation

    def test_post_observations_bulk(self):
        # Prepare data for multiple observations
        observations_data = [
            {
                'user': self.user.id,
                'date': '2023-04-02',
                'time': '14:00:00',
                'timeZoneOffset': "+01:00",
                'location': "Bulk Location 1",
                'temperatureLandSurface': 23.0,
                'temperatureSeaSurface': 24.0,
                'humidity': 70.0,
                'windSpeed': 12.0,
                'windDirection': "SW",
                'precipitation': 3.0,
                'haze': 8.0,
                'notes': "Bulk observation notes 1."
            },
            {
                'user': self.user.id,
                'date': '2023-04-02',
                'time': '14:30:00',
                'timeZoneOffset': "+01:00",
                'location': "Bulk Location 2",
                'temperatureLandSurface': 24.0,
                'temperatureSeaSurface': 25.0,
                'humidity': 68.0,
                'windSpeed': 11.0,
                'windDirection': "SE",
                'precipitation': 3.5,
                'haze': 9.0,
                'notes': "Bulk observation notes 2."
            }
        ]

        response = self.client.post('/observations/bulk/', observations_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 2)  # Check if 2 observations were returned in the response
        # Optionally, verify that the response data matches what was posted
        for i, observation_data in enumerate(observations_data):
            for key in observation_data:
                if key != 'user':  # Excluding user as it's not returned in the serializer data
                    self.assertEqual(str(response.data[i][key]), str(observation_data[key]))

    def test_bulk_observation_incomplete_data(self):
        # Test to ensure validation works for bulk posts with incomplete data
        incomplete_data = [
            {
                'user': self.user.id,
                'date': '2023-04-02',
                # Missing 'time' and other required fields
                'location': "Missing Data Location",
            }
        ]

        response = self.client.post('/observations/bulk/', incomplete_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
