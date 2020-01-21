#!/usr/bin/python3
""" Module for reading lines """

def read_lines(filename="", nb_lines=0):
    """ With """
    count = 0
    with open(filename, "r", encoding='utf8') as f:
        for line in f:
            print("{}".format(line), end="")
            count += 1
            if (count == nb_lines):
                break
        f.close()
