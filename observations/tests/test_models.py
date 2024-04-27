from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date, time
from .models import Observation

User = get_user_model()

class ObservationModelTests(TestCase):

    def setUp(self):
        # Create a user instance to use for creating an Observation
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        
        # Create an observation instance
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

    def test_observation_creation(self):
        # Test that the observation instance can be created properly
        self.assertEqual(self.observation.user.username, 'testuser')
        self.assertEqual(self.observation.date, date.today())
        self.assertEqual(self.observation.timeZoneOffset, "+00:00")
        self.assertEqual(self.observation.location, "Test Location")
        self.assertEqual(self.observation.temperatureLandSurface, 25.5)
        self.assertEqual(self.observation.temperatureSeaSurface, 26.5)
        self.assertEqual(self.observation.humidity, 75.00)
        self.assertEqual(self.observation.windSpeed, 10.5)
        self.assertEqual(self.observation.windDirection, "NE")
        self.assertEqual(self.observation.precipitation, 2.5)
        self.assertEqual(self.observation.haze, 10.2)
        self.assertEqual(self.observation.notes, "Sample observation notes.")

    def test_string_representation(self):
        # Test that the custom string representation method works correctly
        self.assertEqual(str(self.observation), f"Observation - {self.observation.date} {self.observation.time}")
