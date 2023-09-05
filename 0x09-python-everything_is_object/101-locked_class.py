#!/usr/bin/python3
"""
A class LockedClass that only takes first name as the 
only attribute and prevents dynamic addition of any
other attributes
"""


class LockedClass:
    """class that does not allow dynamic addition of
    attributes"""

    __slots__ = ['first_name']
