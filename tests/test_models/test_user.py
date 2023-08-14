#!/usr/bin/python3
"""
This module defines the User class.
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """Test the attributes of the User class."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
