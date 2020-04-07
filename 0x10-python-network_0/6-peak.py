#!/usr/bin/python3
"""
Docstring
"""


def find_peak(ln):
    """
    Trojan
    """
    length = len(ln) - 1

    if not ln:
        return None

    if ln[0] >= ln[1]:
        return ln[0]

    if ln[length] > ln[length - 1]:
        return ln[length]

    for i in range(1, length):
        if ln[i] > ln[i + 1] and ln[i] > ln[i - 1]:
            return(ln[i])

    return None
