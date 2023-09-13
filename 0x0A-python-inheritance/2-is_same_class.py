#!/usr/bin/python3
"""module that checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """
    Function checks if an object is an instance of a specified class

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
