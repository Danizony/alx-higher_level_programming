#!/usr/bin/python3
""" This defines a function """


def lookup(obj):
    """
    Function that returns the list of available attributes
    and methods of an object

    Arg:
    obj - object passed as an argument.

    Returns: List of attributes and methods
    """
    attributes_and_methods = dir(obj)

    list_attributes_methods = []

    for name in attributes_and_methods:
        if not name.startswith('_'):
            list_attributes_methods.append(name)
    return list_attributes_methods
