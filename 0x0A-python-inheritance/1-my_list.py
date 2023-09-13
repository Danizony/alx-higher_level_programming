#!/usr/bin/python3
"""This module inherits from a list class"""


class MyList(list):
    """class that inherits from a list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
