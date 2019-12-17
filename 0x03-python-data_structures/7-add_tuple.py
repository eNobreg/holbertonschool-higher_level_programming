#!/usr/bin/python3


def add_tuple(a=(), b=()):
    new_1 = a + ("0", "0")
    new_2 = b + ("0", "0")

    sumA = int(new_1[0]) + int(new_2[0])
    sumB = int(new_1[1]) + int(new_2[1])
    return sumA, sumB
