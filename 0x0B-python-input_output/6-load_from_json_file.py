#!/usr/bin/python3
"""
Python module that creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file: A function that creates an object
    back from a JSON file
    Arg:
        filename: the file to read
    """

    with open(filename, "r") as f:
        return json.load(f)
