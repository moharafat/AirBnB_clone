#!/usr/bin/python3
""" test module for place.py
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class to test the Place module
    """

    def test_place_city_id(self):
        """test Place city_id
        """
        self.assertEqual(str, type(Place.city_id))

    def test_place_user_id(self):
        """test Place user_id
        """
        self.assertEqual(str, type(Place.user_id))

    def test_place_name(self):
        """test Place name
        """
        self.assertEqual(str, type(Place.name))

    def test_place_description(self):
        """test Place description
        """
        self.assertEqual(str, type(Place.description))

    def test_place_number_rooms(self):
        """test Place number_rooms
        """
        self.assertEqual(int, type(Place.number_rooms))

    def test_place_number_bathrooms(self):
        """test Place number_bathrooms
        """
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_place_max_guest(self):
        """test Place max_guest
        """
        self.assertEqual(int, type(Place.max_guest))

    def test_place_price_by_night(self):
        """test Place price_by_night
        """
        self.assertEqual(int, type(Place.price_by_night))

    def test_place_latitude(self):
        """test Place latitude
        """
        self.assertEqual(float, type(Place.latitude))

    def test_place_longitude(self):
        """test Place longitude
        """
        self.assertEqual(float, type(Place.longitude))

    def test_place_amenity_ids(self):
        """test Place amenity_ids
        """
        self.assertEqual(list, type(Place.amenity_ids))
