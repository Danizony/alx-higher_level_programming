#!/usr/bin/python3
"""This module defines object representation by json string"""
import json


def from_json_string(my_str):
    """this returns an object repesented by a JSON string"""
    python_data = json.loads(my_str)
    return python_data
