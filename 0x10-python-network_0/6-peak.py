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

    return (rec_check(ln, length // 2, length))
def rec_check(ln, start, end):
    """
    Recursive function to check"
    """
    for i in range(start, end):
        if ln[i] > ln[i + 1] and ln[i] > ln[i - 1]:
            return(ln[i])
    rec_check(1, start - 1)

