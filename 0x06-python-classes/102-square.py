#!/usr/bin/python3

# Build-up on the square from Mandatory tasks
"""Defines and builds a square"""


class Square:
    """Further defines a square by enabling it answer to
    comparators"""

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

    def __eq__(self, other):
        """Compares two different squares"""
        return self.area() == other.area()

    def __It__(self, other):
        """Checking is subj square is larger"""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if subj square is smaller or equal to"""
        return self.area() <= other.area()

    def __ne__(self, other):
        """Checks if no two squares are equal"""
        return self.area() != other.area()

    def __gt__(self, other):
        """ Checking is subj square is largest"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if the subj square is largest of equal to others"""
        return self.area() >= other.area()
