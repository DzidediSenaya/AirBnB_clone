#!/usr/bin/python3
"""
This module defines the FileStorage class.
"""

import unittest
import os
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after each test."""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the 'all' method."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """Test the 'new' method."""
        obj = BaseModel()
        self.storage.new(obj)
        obj_key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(obj_key, self.storage._FileStorage__objects)

    def test_save_reload(self):
        """Test the 'save' and 'reload' methods."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        obj_key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(obj_key, new_storage._FileStorage__objects)

    def test_reload_nonexistent_file(self):
        """Test 'reload' when file doesn't exist."""
        new_storage = FileStorage()
        new_storage.reload()

    def test_reload_empty_file(self):
        """Test 'reload' with an empty JSON file."""
        with open(FileStorage._FileStorage__file_path, "w") as f:
            f.write("")

        new_storage = FileStorage()
        new_storage.reload()


if __name__ == "__main__":
    unittest.main()
