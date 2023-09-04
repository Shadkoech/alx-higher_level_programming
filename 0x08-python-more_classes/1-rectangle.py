#!/usr/bin/python3
"""
Class function that defines a Rectangle by:
    - Private instance attribute width
    - Private instance attribute height
The width and height must be integers otherwise
Raises:
    TypeError: width must be an integer
    TypeError: height must be an integer
"""


class Rectangle:
    """Class definition called Rectangle with privately set
    width and height attributes
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
