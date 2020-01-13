#!/usr/bin/python3
""" Function to divide a matrix  """


def matrix_divided(matrix, div):
    """ Divide a Matrix and check Errors """

    if div is 0:
        raise ZeroDivisionError("division by zero")  
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for m_list in matrix:
        if isinstance(m_list, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        if len(m_list) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        if not all(isinstance(x, (int, float)) for x in m_list):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    for i in range(len(matrix)):
        if (i != 0):
            c = i - 1
            if len(matrix[i]) != len(matrix[c]):
                raise TypeError("Each row of the matrix must have the "
                                "same size")

    return [[round(i / div, 2) for i in m_list] for m_list in matrix]
