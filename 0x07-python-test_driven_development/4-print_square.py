#!/usr/bin/python
"""
print_square - Function that prints a square with the character #
Arg:
    size - The length of the square
Raises exceptions:
    - TypeError when size is not an integer
    - ValueError is size is less than zero
    - TypeError when size is a float and less than 0
"""


def print_square(size):
    """
    A function that prints a square using # symbol
    Should not import any module
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        for y in range(size):
            print("#", end="")

        print()
