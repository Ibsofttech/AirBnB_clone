#!/usr/bin/env python3
""" module that defines a subclass City from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Defines the class City"""
    state_id = ""
    name = ""
