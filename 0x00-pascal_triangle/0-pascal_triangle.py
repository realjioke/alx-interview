#!/usr/bin/python3
""" This module documents the python implementation of the pascals triangle """


def pascal_triangle(n):
    """ A Pascal's triangle function by list comprehension expansion """

    triangle = []
    if n <= 0:
        return []

    start = [1]
    triangle.append(start)
    if n == 1:
        return triangle

    for i in range(n - 1):
        start = [start[i] + start[i + 1] for i in range(0, len(start) - 1)]
        start.insert(0, 1)
        start.append(1)
        triangle.append(start)

    return triangle
