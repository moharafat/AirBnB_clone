#!/usr/bin/env python3
"""Amenity module containing class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """To create a new Amenity

    Args:
        BaseModel (BaseModel): super of class Amenity
    """
    name = ""
