#!/usr/bin/python3
"""
This module defines a new class Rectangle which actually inherits
fr0m a previously established Basegeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    New class that is a child/derived class of BaseGeometry
    Has attributes width and height
    """

    def __init__(self, width, height):
        """class constructor for initializing Rectangle's width and Height

        Args:
            width(int): width of Rectangle
            height(int): height of Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """implementing area of the Rectangle
        method already defined in baseclass
        """
        return self.__width * self.__height

    def __str__(self):
        """returns string representation of the Rectangle
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
