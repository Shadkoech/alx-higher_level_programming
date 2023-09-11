#!/usr/bin/python3
"""
def lookup(obj): function that returns list of available attributes and methods
Arg:
    obj - An instance of the class to get list attributes and methods
Return:
    list of attributes and methods
"""


def lookup(obj):
    """
    This is the object to extract and list all the available
    attributes and methods
    """
    return dir(obj)
