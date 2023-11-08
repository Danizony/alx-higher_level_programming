#!/usr/bin/python3
"""This module defines a class called Student"""


class Student:
    """This represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This gets a dictionary representation of the Student
        If attrs is a list of strings, represents only those atrributes
        in the list
        """
        if (type(attrs) == list and
                all(type(elements) == str for elements in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
