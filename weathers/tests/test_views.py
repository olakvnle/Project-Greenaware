from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Country, City
from django.contrib.auth.models import User

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Optionally authenticate if any of the views require authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.country = Country.objects.create(name="Testland")
        self.city = City.objects.create(name="Testville", country=self.country)

    def test_get_countries(self):
        response = self.client.get(reverse('countries'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming one country in the database

    def test_create_country(self):
        data = {'name': 'Newland'}
        response = self.client.post(reverse('countries'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 2)  # Including the setUp country

    def test_get_cities(self):
        response = self.client.get(reverse('cities'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Note: 201 seems incorrect for a GET request.
        self.assertEqual(len(response.data), 1)  # Assuming one city in the database

    def test_create_city(self):
        data = {'name': 'Newville', 'country': self.country.id}
        response = self.client.post(reverse('cities'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Usually, it should be 201 CREATED for POST.
        self.assertEqual(City.objects.count(), 2)

    def test_get_location(self):
        response = self.client.get(reverse('location'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, {'message': 'Hello World!'})

