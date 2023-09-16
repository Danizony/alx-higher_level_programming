#!/usr/bin/python3
"""This module defines a JSON file reading"""
import json


def load_from_json_file(filename):
    """this function reads from a JSON file"""
    with open(filename, 'r') as json_file:
        return json.load(json_file)
