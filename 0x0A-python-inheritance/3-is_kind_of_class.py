#!/usr/bin/python3
"""Module that checks if object is an instance or a sub-class of a class"""


def is_kind_of_class(obj, a_class):
    """
    Function checks if an object is an instance of, or inherits from, a
    specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or inherits from it;
        False otherwise.
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
