#!/usr/bin/python3
"""This defines the locked class"""


class LockedClass:
    """
    Only allows instantiation of an attribute called first_name
    """

    __slots__ = ["first_name"]
