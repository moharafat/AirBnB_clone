#!/usr/bin/python3
""" test module for user.py
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class to test the User module
    """

    def test_email(self):
        """test User email
        """
        self.assertEqual(str, type(User.email))

    def test_password(self):
        """test User password
        """
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        """test User first_name
        """
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        """test User last_name
        """
        self.assertEqual(str, type(User.last_name))
