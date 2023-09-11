#!/usr/bin/python3
"""
inherits_from - Function that returns True if object is an instance
of a class that inherited out of a specified class
Args:
    obj - The object instance
    a_class - particular class to check
Return:
    True if object is an instance
    False otherwise
"""


def inherits_from(obj, a_class):
    """
    checks if object is an instance of class direct or got inherited
    out of another class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
