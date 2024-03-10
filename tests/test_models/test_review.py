#!/usr/bin/python3
""" test module for review.py
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Class to test the Review module
    """

    def test_review_place_id(self):
        """test Review place_id
        """
        self.assertEqual(str, type(Review.place_id))

    def test_review_user_id(self):
        """test Review user_id
        """
        self.assertEqual(str, type(Review.user_id))

    def test_review_text(self):
        """test Review text
        """
        self.assertEqual(str, type(Review.text))
