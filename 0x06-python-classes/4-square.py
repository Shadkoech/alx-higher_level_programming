#!/usr/bin/python3

# A Build-up on the square from Q-3
"""Defines a square"""


class Square:
    """Further defines a square by using property
    setter to set private instance size"""

    def __init__(self, size=0):
        """size attribute must be an integer and
        larger than zero"""
        self.__size = size

    @property
    def size(self):
        """This method retrieves square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method that sets square size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """"Calc and returns the area of the square"""
        return (self.__size ** 2)
