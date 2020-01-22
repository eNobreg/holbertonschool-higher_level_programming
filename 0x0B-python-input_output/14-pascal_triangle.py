#!/usr/bin/python3
""" Triangle Print """


def pascal_triangle(n):
    """ Making a matrix """

    new_list = []
    matrix = []
    if n == None:
        return []
    if n <= 0:
        return []
    for j in range(1, n + 1):
        num = 1
        for i in range(1, j + 1):
            new_list.append(num)
            num = int(num * (j - i) / i)
        matrix.append(new_list)
        new_list = []
    return matrix
