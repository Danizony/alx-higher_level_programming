#!/usr/bin/python3
"""This module defines a file append function"""


def append_write(filename="", text=""):
    """This appends a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
