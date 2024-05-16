from django.test import SimpleTestCase
from django.urls import resolve, reverse
from weathers.views import Countries, Cities, Location

class URLTests(SimpleTestCase):

    def test_country_list_url(self):
        """Test the URL for listing countries is resolved to the correct view"""
        resolver = resolve('/api/v1/countries/')
        self.assertEqual(resolver.func.view_class, Countries)

    def test_city_list_url(self):
        """Test the URL for listing cities is resolved to the correct view"""
        resolver = resolve('/api/v1/cities/')
        self.assertEqual(resolver.func.view_class, Cities)

    def test_location_url(self):
        """Test the URL for the location view is resolved to the correct view"""
        # Since 'locations/' doesn't have a name, use the full path to test
        resolver = resolve('/api/v1/locations/')
        self.assertEqual(resolver.func.view_class, Location)

