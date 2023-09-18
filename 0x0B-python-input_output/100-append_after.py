#!/usr/bin/python3
"""This module defines a text file insertion"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file
    """
    text = ""
    with open(filename) as v:
        for line in v:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
