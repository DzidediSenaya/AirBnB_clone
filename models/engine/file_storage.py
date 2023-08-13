#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def serialize(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(serialized, f)

    def deserialize(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                deserialized = json.load(f)
                for key, value in deserialized.items():
                    class_name = value['__class__']
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        else:
            cls_objects = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    cls_objects[key] = value
            return cls_objects

    def reload(self):
        """Reloads objects from the JSON file"""
        self.deserialize()


# Initialize FileStorage instance
storage = FileStorage()
storage.deserialize()  # Load data from JSON file
