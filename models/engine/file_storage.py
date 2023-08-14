#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    A class for serializing and deserializing instances to/from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary of all objects.

        Returns:
            dict: Dictionary containing all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set a new object in the dictionary.

        Args:
            obj: The object to be added to the dictionary.
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Serialize __objects to the JSON file.
        """
        odict = {key: val.to_dict() for key, val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(odict, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects.

        This method reads the contents of the JSON file, deserializes the data,
        and recreates instances of objects in the __objects dictionary.
        If the JSON file is not found, no exception is raised.
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for key, val in objdict.items():
                    cls_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(cls_name)(**val))
        except FileNotFoundError:
            pass
