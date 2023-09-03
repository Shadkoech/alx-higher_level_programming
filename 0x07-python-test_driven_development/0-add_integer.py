#!/usr/bin/python3
"""add_integer - function that adds 2 integers
Args:
    a (int/float): This is the first parameter
    b (int/float): initialized to 98 
Returns: a + b """


def add_integer(a, b=98):
    """
    Raises: TypeError: if a or b is not an integer/float
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)

    return (a + b)
