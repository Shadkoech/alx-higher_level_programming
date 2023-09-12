#!/usr/bin/python3
"""
Function that reads a text file using UTF-8
"""

def read_file(filename=""):
    """
    read_file - function that read a text file using UTF-8
    and prints it to stdout
    Args:
        Filename - The name of the file to be read
    """

    with open(filename, encoding="utf-8") as f:
        textfile= f.read()
        print(textfile, end="")
