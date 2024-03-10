#!/usr/bin/env python3
"""State module containing class State that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """To create a new State

    Args:
        BaseModel (BaseModel): super of class State
    """

    name = ""
