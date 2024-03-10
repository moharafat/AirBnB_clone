#!/usr/bin/python3
""" test module for state.py
"""
import unittest
from datetime import datetime
import io
import sys
import uuid
from models.state import State


class TestState(unittest.TestCase):
    """Class to test the State module
    """

    def test_state_name(self):
        """test State email
        """
        self.assertEqual(str, type(State.name))
