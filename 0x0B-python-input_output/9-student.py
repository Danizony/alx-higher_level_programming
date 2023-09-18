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

    def to_json(self):
        """Gets a dictionary representation of a student"""
        return self.__dict__
