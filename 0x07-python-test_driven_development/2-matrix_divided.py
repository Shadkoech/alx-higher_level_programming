#!/usr/bin/python3
"""matrix_divided: Function that divides all elements of a matrix
Args:
    Matrix - A list of integers or floats
    div - a divisor applied on the members of the matrix
Returns: A new matrix of divided up elements"""


def matrix_divided(matrix, div):
    """
    Raises:
        TypeError("matrix must be a matrix (list of lists) of integers/floats")
        TypeError("Each row of the matrix must have the same size")
        TypeError("div must be a number")
        """
    valrow = [all(isinstance(x, (int, float)) for x in row) for row in matrix]
    if not all(isinstance(row, list) and valrow for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # checking the length of the rows
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # checking if div is an int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

        # creating new matrix from divide elements
    new_matrix = []
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
