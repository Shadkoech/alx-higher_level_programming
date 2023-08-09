#!/usr/bin/python3

def magic_calculation(a, b, c):
    """The code must duplicate a given python bytecode"""

# First it checks if a is less than b
# If so, return value of c
    if (a < b):
        return c
# If not, it then checks if c is great than b
# If true, it returns the sum of a and b
    elif (c > b):
        return (a + b)

# if none of the two conditions above are true
# it returns the result of ((a * b) - c)
    return ((a * b) - c)
