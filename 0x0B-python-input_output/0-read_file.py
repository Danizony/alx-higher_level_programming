#!/usr/bin/python3
"""
Module contains function that reads a text file and prints in
a stdout
"""


def read_file(filename=""):
    """this function reads text file and prints it"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
