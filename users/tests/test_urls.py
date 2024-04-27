from django.test import SimpleTestCase
from django.urls import resolve
from users.views import CustomTokenObtainPairView, CustomTokenRefreshView, CustomTokenVerifyView, LogoutView

class JWTURLsTests(SimpleTestCase):

    def test_jwt_create_url_resolves(self):
        # Test the URL for obtaining a JWT
        resolver = resolve('/jwt/create/')
        self.assertEqual(resolver.func.view_class, CustomTokenObtainPairView)

    def test_jwt_refresh_url_resolves(self):
        # Test the URL for refreshing a JWT
        resolver = resolve('/jwt/refresh/')
        self.assertEqual(resolver.func.view_class, CustomTokenRefreshView)

    def test_jwt_verify_url_resolves(self):
        # Test the URL for verifying a JWT
        resolver = resolve('/jwt/verify/')
        self.assertEqual(resolver.func.view_class, CustomTokenVerifyView)

    def test_logout_url_resolves(self):
        # Test the URL for logging out
        resolver = resolve('/logout/')
        self.assertEqual(resolver.func.view_class, LogoutView)
