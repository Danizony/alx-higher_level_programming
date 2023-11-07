#!/usr/bin/python3
"""
    This module returns True if the object is exactly
    an instance of the specified class; otherwise False
"""


def is_same_class(obj, a_class):
    """This function gets the instance and returns True or False"""
    return (type(obj) == a_class)
