#!/usr/bin/python3

# This question is based on 0-square.py
"""The class Square is given its size"""


class Square:
    """This is a class square with defined size. The size is
    very crucial to a square and it is kept private to preserve control"""

    def __init__(self, size):
        """initialization method for an instance
        it takes a private argument size without a value or
        verification"""

        self.__size = size
