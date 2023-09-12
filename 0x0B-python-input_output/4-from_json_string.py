#!/usr/bin/python3
"""
Python module that returns Python object previous
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    from_json_string: A function that returns an object represented
    by JSON string
    Args:
        my_str: json string to take it back to str
    """

    return json.loads(my_str)
