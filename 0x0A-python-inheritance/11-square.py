#!/usr/bin/python3
"""
This is a new class Square that inherits fr0m class
Rectangle which inherits From class BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square is a subclass of Rectangle """

    def __init__(self, size):
        """square size initialization
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """computes area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """prints the string representation of a square
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
