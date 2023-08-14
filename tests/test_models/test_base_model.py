#!/usr/bin/python3
"""
This module contains test cases for the BaseModel class and its methods.
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_base_model_attributes(self):
        """
        Test attributes creation in BaseModel instance.
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_base_model_save(self):
        """
        Test the save method's functionality.
        """
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_base_model_to_dict(self):
        """
        Test the to_dict method's functionality.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        model_dict = my_model.to_dict()

        self.assertEqual(model_dict['name'], "My First Model")
        self.assertEqual(model_dict['my_number'], 89)
        self.assertEqual(model_dict['__class__'], "BaseModel")

    def test_recreate_instance_from_dict(self):
        """
        Test recreating an instance from its dictionary representation.
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_dict = my_model.to_dict()

        new_model = BaseModel(**my_model_dict)

        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(my_model.id, new_model.id)
        self.assertEqual(my_model.created_at, new_model.created_at)
        self.assertEqual(my_model.updated_at, new_model.updated_at)
        self.assertEqual(my_model.name, new_model.name)
        self.assertEqual(my_model.my_number, new_model.my_number)


if __name__ == '__main__':
    unittest.main()
