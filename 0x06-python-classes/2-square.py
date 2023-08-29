#!/usr/bin/python3

# A build up on previous 1-square.py
""" A representation of a class square that defines a squarein the following ways"""


class Square:
    """This class defines a square by the following"""

    def __init__(self, size=0):
        """size attribute must be an integer and more than zero"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
