#!/usr/bin/python3
"""This module contains function that reads a text file
and prints it to stdout.
"""


def read_file(filename=""):
    """This prints the contents of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
