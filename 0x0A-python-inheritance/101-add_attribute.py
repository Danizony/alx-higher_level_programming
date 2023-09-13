#!/usr/bin/python3
"""This module defines a function that adds attributes to objects"""


def add_attribute(obj, attr, value):
    """adds new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
