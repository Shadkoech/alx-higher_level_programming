#!/usr/bin/python3
"""
Creation of new class inheriting fr0m Basegeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    New class that is a child/derived class of BaseGeometry
    """
    def __init__(self, width, height):
        """class constructor for initializing Rectangle's width and Height
        Args:
            width(int): width of Rectangle
            height(int): height of Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
