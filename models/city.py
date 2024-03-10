#!/usr/bin/env python3
"""City module containing class City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """To create a new City

    Args:
        BaseModel (BaseModel): super of class City
    """
    state_id = ""
    name = ""
