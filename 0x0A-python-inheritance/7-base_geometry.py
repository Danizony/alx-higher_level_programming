#!/usr/bin/python3
"""Module containing a basegeometry class"""


class BaseGeometry:
    """this class represents a base geometry"""

    def area(self):
        """this method is yet to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ this method validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
