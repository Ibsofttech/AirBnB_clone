#!/usr/bin/env python3
""" A module that inherits BaseModel to create new user"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
