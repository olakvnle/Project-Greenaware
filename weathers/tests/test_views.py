from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from users.models import UserAccount
from weathers.models import Country, City
from django.contrib.auth.models import User

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Optionally authenticate if any of the views require authentication
        self.user = UserAccount.objects.create_user(email='testuser@example.com', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.country = Country.objects.create(name="Testland")
        self.city = City.objects.create(name="Testville", country=self.country)

    def test_get_countries(self):
        # Assuming the URL mapped to the countries view is '/countries/'
        response = self.client.get('/api/v1/countries/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming one country in the database

    def test_create_country(self):
        data = {'name': 'Newland'}
        # Assuming the URL mapped to the countries view is '/countries/'
        response = self.client.post('/api/v1/countries/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 2)  # Including the setUp country

    # def test_get_cities(self):
    #     # Assuming the URL mapped to the cities view is '/cities/'
    #     response = self.client.get('/api/v1/cities/')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Note: 201 seems incorrect for a GET request.
    #     self.assertEqual(len(response.data), 1)  # Assuming one city in the database

    # def test_create_city(self):
    #     data = {'name': 'Newville', 'country': self.country.id}
    #     # Assuming the URL mapped to the cities view is '/cities/'
    #     response = self.client.post('/api/v1/cities/', data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Usually, it should be 201 CREATED for POST.
    #     self.assertEqual(City.objects.count(), 2)

    # def test_get_location(self):
    #     # Assuming the URL mapped to the location view is '/location/'
    #     response = self.client.get('/api/v1/location/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertDictEqual(response.data, {'message': 'Hello World!'})
