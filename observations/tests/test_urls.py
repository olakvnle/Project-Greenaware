from django.test import SimpleTestCase
from django.urls import resolve
from observations.views import Observations, ObservationsBulk, UserObservations, ObservationDetail

class ObservationUrlsTests(SimpleTestCase):

    def test_observations_url_resolves(self):
        # Direct URL for the Observations view
        self.assertEqual(resolve('/observations/').func.view_class, Observations)

    def test_observation_detail_url_resolves(self):
        # Direct URL for the ObservationDetail view, assuming '1' is a possible primary key
        self.assertEqual(resolve('/observations/1/').func.view_class, ObservationDetail)

    def test_user_observations_url_resolves(self):
        # Direct URL for the UserObservations view, assuming 'user-123' is a possible user ID
        self.assertEqual(resolve('/observations/user/user-123').func.view_class, UserObservations)

    def test_observations_bulk_url_resolves(self):
        # Direct URL for the ObservationsBulk view
        self.assertEqual(resolve('/observations/bulk/').func.view_class, ObservationsBulk)
