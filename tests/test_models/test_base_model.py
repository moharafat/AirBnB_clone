#!/usr/bin/python3
""" test module for base_model.py
"""
import unittest
from datetime import datetime
import io
import sys
import uuid
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Class to test the BaseModel module
    """

    def test_init_kwargs(self):
        """test uuid
        """
        bm = BaseModel(
            id=str(uuid.uuid4),
            created_at=datetime.today(),
            updated_at=datetime.today()
            )
        self.assertIsInstance(bm, BaseModel)

    def test_uuid(self):
        """test uuid
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_created_at(self):
        """test created at
        """
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertIsInstance(bm1.created_at, datetime)

    def test_updated_at(self):
        """test updated at
        """
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_str_method(self):
        """test string method
        """
        bm1 = BaseModel()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(bm1)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        captured_output.close()
        self.assertEqual(
            output, f"[{bm1.__class__.__name__}] ({bm1.id}) {bm1.__dict__}\n"
            )

    def test_save_method(self):
        """test save method
        """
        bm1 = BaseModel()
        old_updated = bm1.updated_at
        self.assertEqual(bm1.updated_at, old_updated)
        bm1.save()
        self.assertNotEqual(bm1.updated_at, old_updated)

    def test_to_dict_method(self):
        """test to dict method
        """
        bm1 = BaseModel()
        my_dict = bm1.to_dict()
        self.assertIn('id', my_dict)
        self.assertIn('created_at', my_dict)
        self.assertIn('updated_at', my_dict)
        self.assertIn('updated_at', my_dict)
        self.assertIn('__class__', my_dict)
        self.assertEqual(my_dict['id'], bm1.id)
        self.assertEqual(my_dict['created_at'], bm1.created_at.isoformat())
        self.assertEqual(my_dict['updated_at'], bm1.updated_at.isoformat())
        self.assertEqual(my_dict['__class__'], bm1.__class__.__name__)

    def test_create_instance_from_dict(self):
        """test creating an instance from a dict
        """
        bm1 = BaseModel()
        bm1.name = 'my base model'
        bm1.number = 89
        my_dict = bm1.to_dict()
        bm2 = BaseModel(**my_dict)
        self.assertEqual(bm2.id, bm1.id)
        self.assertEqual(bm2.created_at, bm1.created_at)
        self.assertEqual(bm2.updated_at, bm1.updated_at)
        self.assertEqual(bm2.name, bm1.name)
        self.assertEqual(bm2.number, bm1.number)
        self.assertEqual(bm2.to_dict(), bm1.to_dict())
        self.assertNotEqual(bm1, bm2)
