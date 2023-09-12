#!/usr/bin/python3
"""
This is a module that implements JSON string representation
"""
import json


def to_json_string(my_obj):
    """
    to_json_string: a function that returns the JSON representation
    of an object string
    Args:
        my_obj - The object string to do JSON formatting
    Returns:
        JSON formatted string
    """

    return json.dumps(my_obj)
