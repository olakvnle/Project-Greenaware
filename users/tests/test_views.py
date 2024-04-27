from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import UserAccount
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class CustomJWTViewsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass123')
        self.token = RefreshToken.for_user(self.user)

    def test_token_obtain_pair_view(self):
        url = reverse('token_obtain_pair')
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.cookies)
        self.assertIn('refresh', response.cookies)

    def test_token_refresh_view(self):
        url = reverse('token_refresh')
        refresh_token = str(self.token.refresh_token)
        self.client.cookies['refresh'] = refresh_token
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('access', response.cookies)

    def test_token_verify_view(self):
        url = reverse('token_verify')
        access_token = str(self.token.access_token)
        self.client.cookies['access'] = access_token
        response = self.client.post(url, {'token': access_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout_view(self):
        url = reverse('logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn('access', response.cookies)
        self.assertNotIn('refresh', response.cookies)