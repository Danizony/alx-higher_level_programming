#!/usr/bin/python3
"""This module checks if an object is an instance
of a class or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """This function returns true if object
    is an instance of a class or from an inherited
    class
    """
    return (isinstance(obj, a_class))
