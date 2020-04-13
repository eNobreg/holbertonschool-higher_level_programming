#!/usr/bin/python3
"""
Docstrig
"""

from urllib import request
import sys


with request.urlopen(sys.argv[1]) as response:
    print(response.info()['X-Request-Id'])
