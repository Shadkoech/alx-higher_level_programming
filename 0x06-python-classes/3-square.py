#!/usr/bin/python3

# Build-up on the square from Q2
# Not allowed to import module
"""Defines a square"""


class Square:
    """Further defines a square by use of
    public instance method"""

    def __init__(self, size=0):
        """size attribute must be an integer and more than zero"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calc and returns the area of the square"""
        return self.__size ** 2
