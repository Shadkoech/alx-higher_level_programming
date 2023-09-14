#!/usr/bin/python3
"""
A module that creates and represents a Pascal's triangle
"""


def pascal_triangle(n):
    """
    A function that returns a list of integers that
    represent a Pascal's triangle
    Args:
        n - number of elements
    Returns:
        Empty List if  n <= 0
    """

    if n <= 0:
        return []

    pascal_triangle = [[1]]
    # in order to rep rows in the pascals tri, we iterate from 1 t0 n-1
    for i in range(1, n):
        # process of first initializing each other row
        pascalrow = [1]
        prevrow = pascal_triangle[i - 1]

        for j in range(1, i):
            """we now iterate from j=1 to i-1 and each time
            we add elements from previus row and then add them
            to next row. We must then add 1, at end of each
            given row """

            pascalrow.append(prevrow[j - 1] + prevrow[j])

        # we then append each row and return the triangle list
        pascalrow.append(1)
        pascal_triangle.append(pascalrow)

    return pascal_triangle
