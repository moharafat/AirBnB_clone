#!/usr/bin/env python3
"""user module containing class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """To create a new user

    Args:
        BaseModel (BaseModel): super of class User
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
