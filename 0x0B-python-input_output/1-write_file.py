#!/usr/bin/python3
"""
This is a module that creates a file and writes a string
to it.
"""


def write_file(filename="", text=""):
    """
    write_file: Function that writes a string to a text file
    Args:
        filename - The name of the file to write to
        text - The text to write out
    Returns:
        Number of characters written
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
