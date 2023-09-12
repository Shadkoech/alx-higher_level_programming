#!/usr/bin/python3
"""
A module that performs JSON serialization
"""


def class_to_json(obj):
    """
    class_to_json: function that returns the dictionary description with some
    data structures(ie lits, dictionaries, strings, int, boolean)
    Args:
        obj - An instance of a class
    """

    return obj.__dict__
