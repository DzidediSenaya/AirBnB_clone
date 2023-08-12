#!/usr/bin/python3
"""This module defines the City class"""

from models.base_model import BaseModel

class City(BaseModel):
    """This class defines the City object attributes"""
    state_id = ""  # it will be the State.id
    name = ""
