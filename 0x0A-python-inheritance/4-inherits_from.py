#!/usr/bin/python3
"""module checks if object is an instance of a class
that inherited from a specified class or not
"""


def inherits_from(obj, a_class):
    """ Function returns true if object is an instance of a class
    that inherited (directly or indirectly) from the specified class,
    otherwise False.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
