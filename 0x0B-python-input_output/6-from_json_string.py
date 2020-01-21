#!/usr/bin/python3
""" MOdule """


import json
def from_json_string(my_str):
    """ Convert json to string """
    if my_str is None or my_str == "":
        return
    string = json.loads(my_str)
    return string
