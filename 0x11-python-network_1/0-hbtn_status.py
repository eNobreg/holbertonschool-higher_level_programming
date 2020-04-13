#!/usr/bin/python3
"""
Docstrig
"""

from urllib import request

with request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(str(type(html))))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf8')))
