#!/usr/bin/python3

"""
a module to divide a matrix


"""


def matrix_divided(matrix, div):
    """
    Divides a matrix by the given input divisor

    @matrix: list of list input
    @div: divisor

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix representing the result of the division.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(message)

    length = 0

    for j in matrix:
        if not isinstance(j, list) or not j:
            raise TypeError(message)

        for k in j:
            if not isinstance(k, (float, int)):
                raise TypeError(message)
        if (length != 0) and len(j) != length:
            raise TypeError("Each row of the matrix must have the same size")
        length = len(j)

    z = list(map(lambda a: list(map(lambda b: round(b / div, 2), a)), matrix))
    return (z)
