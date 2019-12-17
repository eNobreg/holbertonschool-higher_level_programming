#!/usr/bin/python3


def max_integer(my_list=[]):
    last_i = 0
    if not my_list or len(my_list) == 0:
        return None

    for i in my_list:
        if i > last_i:
            last_i = i
    return last_i
