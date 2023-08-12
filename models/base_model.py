#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class definition.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Unused positional arguments.
            **kwargs: Keyword arguments containing attributes to set.

        Attributes:
            id (str): The ID of the instance.
            created_at (datetime): The creation datetime of the instance.
            updated_at (datetime): The last update datetime of the instance.
        """
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute and saves the instance to storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary containing the instance attributes.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        obj_dict['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A formatted string containing class name, ID, and attributes.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
