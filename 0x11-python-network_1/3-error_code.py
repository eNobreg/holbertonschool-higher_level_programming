#!/usr/bin/python3
"""
Docstrig
"""
from urllib import error
from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
