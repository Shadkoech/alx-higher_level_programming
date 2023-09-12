#!/usr/bin/python3
"""
Python module that uses JSON representation to write
an object into text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file: A function that writes an object to
    text file using JSON
    Args:
        my_obj: the object to write
        filename: the file to write to
    """

    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)
