#!/usr/bin/python3
""" Test module for file_storage module
"""
import unittest
import pathlib
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test class for FileStorage class
    """
    def test_file_path(self):
        """test file path
        """

        self.assertEqual(
            pathlib.PosixPath, type(FileStorage._FileStorage__file_path)
            )

    def test_object(self):
        """test object attribute
        """
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_new(self):
        """test new method
        """
        bm1 = BaseModel()
        all_objects = storage.all()
        self.assertIn(bm1, all_objects.values())

    def test_all(self):
        """test all method
        """
        self.assertEqual(dict, type(storage.all()))

    def test_save(self):
        """test save method
        """
        bm = BaseModel()
        storage.save()
        self.assertIn(bm, storage.all().values())

    def reload(self):
        """test reload method
        """
        bm = BaseModel()
        storage.reload()
        self.assertIn(bm, storage.all().values())
