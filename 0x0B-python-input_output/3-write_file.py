#!/usr/bin/python3
""" Module for write """


def write_file(filename="", text=""):
    """ Write a file """
    if filename == "":
        return
    with open(filename, "w", encoding='utf8') as f:
        chars = f.write(text)
        f.close()
        return chars
