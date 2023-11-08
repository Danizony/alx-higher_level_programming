#!/usr/bin/python3
"""This module defines a function that appends to a file"""


def append_write(filename="", text=""):
    """This appends a string to the end of a UTF-8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
