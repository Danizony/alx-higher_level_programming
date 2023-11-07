#!/usr/bin/python3
"""This module defines a class that inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class defines rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
