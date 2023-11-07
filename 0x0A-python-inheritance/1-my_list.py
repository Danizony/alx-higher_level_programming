#!/usr/bin/python3
"""This module inherists from the list class"""


class MyList(list):
    """This class inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
