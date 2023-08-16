#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    '''Function computing square value of all integers in a matrix'''
    my_matrix = []

    for row in matrix:
        row_squared = [i ** 2 for i in row]
        my_matrix.append(row_squared)

    return my_matrix
