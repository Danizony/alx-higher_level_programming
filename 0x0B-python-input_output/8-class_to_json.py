#!/usr/bin/python3
"""This module defines a class-to-json function"""


def class_to_json(obj):
    """Returns the dictionary representation of a data structure"""
    return obj.__dict__
