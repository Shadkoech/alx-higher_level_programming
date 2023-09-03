#!/usr/bin/python3
"""
def say_my_name(first_name, last_name=""): A function printing my name
Args:
    first_name - My first name
    last_name -my last name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints my name.
    Raise TypeError if:
        first_name is not a string
        last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
