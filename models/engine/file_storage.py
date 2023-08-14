#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os


class FileStorage:
    """A class for serializing and deserializing instances to/from a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Set a new object in the dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        objects_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, obj_dict in objects_dict.items():
                    class_name, obj_id = key.split(".")
                    cls = globals()[class_name]
                    self.__objects[key] = cls(**obj_dict)
