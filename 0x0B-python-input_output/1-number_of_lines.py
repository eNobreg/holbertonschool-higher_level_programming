#!/usr/bin/python3
""" Module for functions """


def number_of_lines(filename=""):
    """ Function for file reading """
    i = 0
    with open(filename, "r", encoding='utf8') as file_s:
        for line in file_s:
            i += 1
        file_s.close()
    return i
