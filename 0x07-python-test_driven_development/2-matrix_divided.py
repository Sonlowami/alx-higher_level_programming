#!/usr/bin/python3
""" Module containing a matrix diviser"""


def matrix_divided(matrix, div):
    """ Matrix divider function
    args:
        matrix: the list of lists of int or float
        div: the common diviser
    return: new matrix
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    i = 0
    while i < len(matrix) - 1:
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError('each row of the matrix must have the same size')
        i += 1

    try:
        new_matrix = [[round(i / div, 2) for i in row] for row in matrix]
        return new_matrix
    except TypeError:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
