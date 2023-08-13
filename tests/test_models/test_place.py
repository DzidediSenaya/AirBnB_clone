#!/usr/bin/python3
"""Test cases for Place class"""
import unittest
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def test_attributes(self):
        """Test Place attributes"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")


if __name__ == "__main__":
    unittest.main()
