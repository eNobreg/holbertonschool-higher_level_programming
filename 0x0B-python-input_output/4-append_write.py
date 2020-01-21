#!/usr/bin/python3
""" Admin """


def append_write(filename="", text=""):
    """ append file """
    with open(filename, "a", encoding='utf8') as f:
        chars = f.write(text)
        f.close()
        return chars
