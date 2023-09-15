#!/usr/bin/python3
"""This module defines a file-writing function"""


def write_file(filename="", text=""):
    """This writes a string to a text file
    and returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
