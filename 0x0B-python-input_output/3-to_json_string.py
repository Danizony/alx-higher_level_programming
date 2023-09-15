#!/usr/bin/python3
"""This module defines json representation of an object function"""
import json


def to_json_string(my_obj):
    """function that returns json rep of an object"""
    json_data = json.dumps(my_obj)
    return json_data
