#!/usr/bin/python3
"""This module defines how to write an object to a text
file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """this writes an object to a text file using JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f) 
