#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new = my_list[:]
    if idx < 0:
        return new
    elif idx >= len(new):
        return new
    else:
        new[idx] = element
        return(new)
