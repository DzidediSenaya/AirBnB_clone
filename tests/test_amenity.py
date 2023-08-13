#!/usr/bin/python3
"""Test cases for Amenity class"""
import unittest
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_attributes(self):
        """Test Amenity attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
