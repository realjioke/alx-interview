#!/usr/bin/python3
""" Minimum operations required to copy and paste in a file """


def minOperations(n):
    nb_ops = 0
    factor = 2

    if n == 1:
        return 0

    while factor * factor <= n:
        while n % factor == 0:
            nb_ops += factor
            n //= factor
        factor += 1

    if n > 1:
        nb_ops += n

    return nb_ops
