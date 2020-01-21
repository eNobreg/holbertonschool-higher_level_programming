#!/usr/bin/python3
""" Module for functions """


def read_file(filename=""):
    """ Function for file reading """
    with open(filename, "r", encoding='utf8') as file_s:
        for line in file_s:
            print(line, end="")
        file_s.close()
