#!/usr/bin/python3


def add_tuple(a=(), b=()):
    new_1 = a + ("0", "0")
    new_2 = b + ("0", "0")

    return [int(new_1[i]) + int(new_2[i]) for i in range(2)]
