#!/usr/bin/python3
"""
is_kind_of_class - Function that returns True is object is an
instance of child or parent process
Args:
    Obj - The instance object
    a_class - The class to check
Return:
    True if object is an instance
    False otherwise
"""


def is_kind_of_class(obj, a_class):
    """
    Checking if an object is part of a child or parent class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
