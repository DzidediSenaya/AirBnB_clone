#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os


class FileStorage:
    """
    A class for serializing and deserializing
    instances to/from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set a new object in the dictionary."""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
    try:
        with open(FileStorage.__file_path) as f:
            objdict = json.load(f)
            for o in objdict.values():
                cls_name = o["__class__"]
                del o["__class__"]
                self.new(eval(cls_name)(**o))
    except FileNotFoundError:
        raise FileNotFoundError(f"File {FileStorage.__file_path} not found")
