#!/usr/bin/python3
"""
A function that checks if an object is an instance of a class
Args:
    obj - The object instance
    a_class - particular class to check
Returns:
    True - if object is an instance
    False - Otherwise
"""


def is_same_class(obj, a_class):
    """
    checking is an object is part of a class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
