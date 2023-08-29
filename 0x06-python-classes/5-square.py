#!/usr/bin/python3

"""Class that defines a square"""
# Builds from Q-4


class Square:
    """Further defines square by adding a public
    instance method which prints to stdout square
    with # characters"""

    def __init__(self, size=0):
        """The size attr must be an integer and larger than 0"""
        self.__size = size

    @property
    def size(self):
        """Method that retrieves square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """method that sets square size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """"Calc and returns the area of a square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints a square of # to the stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
