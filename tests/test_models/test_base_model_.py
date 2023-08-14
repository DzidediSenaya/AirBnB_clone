#!/usr/bin/python3
"""
This module contains test cases for the BaseModel class and its methods.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A base class that defines common attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance."""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

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
