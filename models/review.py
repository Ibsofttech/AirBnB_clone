#!/usr/bin/env python3
""" module that defines a subclass Review from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines the class Review"""
    place_id = ""
    user_id = ""
    text = ""
