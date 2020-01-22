#!/usr/bin/python3
""" Module """


def append_after(filename="", search_string="", new_string=""):
    """ Function """
    new_line = ""
    with open(filename, "r") as f:
        for line in f:
            new_line += line
            if search_string in line:
                new_line += new_string

    with open(filename, 'w') as f:
        f.write(new_line)
