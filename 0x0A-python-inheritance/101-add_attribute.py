#!/usr/bin/python3
"""Function that adds a new attribute to an object
if it is all possible
Raises:
    TypeError: if object cannot have a new attribute with
    message "can't add new attribute"
"""


def add_attribute(obj, name, attr_value):
    """ adds a new attribute (attr) with a value (attr_value)
    to an object
    Raises error is cannot add the attribute"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, attr_value)
