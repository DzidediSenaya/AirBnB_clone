#!/usr/bin/python3
"""This module defines the Review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """This class defines the Review object attributes"""
    place_id = ""   # it will be the Place.id
    user_id = ""    # it will be the User.id
    text = ""
