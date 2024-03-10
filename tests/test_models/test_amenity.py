#!/usr/bin/python3
""" test module for amenity.py
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class to test the Amenity module
    """

    def test_amenity_name(self):
        """test Amenity name
        """
        self.assertEqual(str, type(Amenity.name))
