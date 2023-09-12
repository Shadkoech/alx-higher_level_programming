#!/usr/bin/python3
"""
This module appends to a file
"""


def append_write(filename="", text=""):
    """
    append_write: a function that appends a string at the end
    of a text file
    Args:
        filename - Name of the file to append to
        text - The text to append
    Returns:
        Number of added char
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
