import json

import what3words
from rest_framework import permissions, status
from rest_framework.response import Response


class WhatThreeWords:
    def __init__(self):
        # Initialize What3words Geocoder with your API key and endpoint
        self.geocoder = what3words.Geocoder("7F2HOJUM")

    def convert_address_coordinate(self, what3word):
        """Convert address to coordinates"""

        # Convert address to coordinates
        data = self.geocoder.convert_to_coordinates(what3word)
        return data
        # coordinates = self.geocoder.convert_to_3wa(what3words.Coordinates(51.484463, -0.195405))

    def process_what3words_response(self, data):
        response = self.convert_address_coordinate(data)
        if 'error' in response:
            error_message = response['error']
            # Handle the error message as needed, such as logging it or raising an exception
            return None, error_message
        else:
            fields_to_extract = ['country', 'nearestPlace', 'coordinates', 'words', 'language', 'map']
            data = {field.replace("nearestPlace", "nearest_place"): response.get(field) for field in fields_to_extract  }

            lat = data['coordinates']['lat']
            lng = data['coordinates']['lng']
            data.pop('coordinates')
            data['lng'] = lng
            data['lat'] = lat
            return data, None

    def get_coordinates(self, what3word):
        data ={
            'coordinate_latitude': what3word.get('lat'),
            'coordinate_longitude': what3word.get('lng'),
            'country': what3word.get('country'),
            'city': what3word.get('nearest_place')
        }

        return data

what3words_instance = WhatThreeWords()
