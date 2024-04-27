from django.test import TestCase
from weathers.models import Country, City, Coordinates, Temperature, Wind, WeatherData
from django.contrib.auth import get_user_model
from users.models import UserAccount


User = get_user_model()

class ModelTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create a user for linking to WeatherData
        cls.user = UserAccount.objects.create_user(email='testuser@example.com', password='testpass123')

        # Create instances of Country and City for use in further relations
        cls.country = Country.objects.create(name='Exampleland')
        cls.city = City.objects.create(name='Exampleville', country=cls.country)

        # Create instances for Coordinates, Temperature, and Wind
        cls.coordinates = Coordinates.objects.create(latitude=40.712776, longitude=-74.005974, city=cls.city)
        cls.temperature = Temperature.objects.create(land_surface=25.5, sea_surface=26.5, city=cls.city)
        cls.wind = Wind.objects.create(speed=5.5, direction='Northeast', city=cls.city)

        # Create a WeatherData instance
        cls.weather_data = WeatherData.objects.create(
            user=cls.user,
            city=cls.city,
            date='2023-04-01',
            time='12:00:00',
            time_zone_offset='+0200',
            coordinates=cls.coordinates,
            temperature=cls.temperature,
            wind=cls.wind,
            precipitation=3.0,
            haze=10.0,
            notes='Sunny day'
        )

    def test_country_creation(self):
        country = Country.objects.create(name='New Exampleland')
        self.assertEqual(country.name, 'New Exampleland')

    def test_city_creation(self):
        city = City.objects.create(name='New Exampleville', country=self.country)
        self.assertEqual(city.name, 'New Exampleville')

    def test_coordinates_creation(self):
        coords = Coordinates.objects.create(latitude=35.6895, longitude=139.6917, city=self.city)
        self.assertEqual(float(coords.latitude), 35.6895)
        self.assertEqual(float(coords.longitude), 139.6917)

    def test_temperature_creation(self):
        temp = Temperature.objects.create(land_surface=28.0, sea_surface=27.0, city=self.city)
        self.assertEqual(float(temp.land_surface), 28.0)
        self.assertEqual(float(temp.sea_surface), 27.0)

    def test_wind_creation(self):
        wind = Wind.objects.create(speed=7.0, direction='Southwest', city=self.city)
        self.assertEqual(float(wind.speed), 7.0)
        self.assertEqual(wind.direction, 'Southwest')

    def test_weather_data_creation(self):
        self.assertEqual(self.weather_data.user.email, 'testuser@example.com')
        self.assertEqual(self.weather_data.city.name, 'Exampleville')
        self.assertEqual(self.weather_data.notes, 'Sunny day')

    def test_country_bulk_create(self):
        countries_data = [{'name': 'Country1'}, {'name': 'Country2'}]
        countries = Country.create_bulk(countries_data)
        self.assertEqual(len(countries), 2)
        self.assertEqual(countries[0].name, 'Country1')
        self.assertEqual(countries[1].name, 'Country2')
