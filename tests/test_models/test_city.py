#!/usr/bin/python3
""" test module for city.py
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class to test the City module
    """

    def test_city_name(self):
        """test City name
        """
        self.assertEqual(str, type(City.name))

    def test_city_state_id(self):
        """test City state_id
        """
        self.assertEqual(str, type(City.state_id))
