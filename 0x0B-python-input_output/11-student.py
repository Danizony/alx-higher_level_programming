#!/usr/bin/python3
"""This module defines a Student class"""


class Student:
    """This represents a student
    """
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of a student
        if attrs is a list of strings, represent only
        those attributes included in the list"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the student
        """
        for i, j in json.items():
            setattr(self, i, j)
