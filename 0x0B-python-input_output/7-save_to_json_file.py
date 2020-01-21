#!/usr/bin/python3
""" This thing """

import json


def save_to_json_file(my_obj, filename):
    """ This file  """
    if (filename is None):
        return
    with open(filename, "w", encoding='utf8') as f:
        json.dump(my_obj, f)
