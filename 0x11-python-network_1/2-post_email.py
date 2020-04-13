#!/usr/bin/python3
"""
Docstrig
"""

from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    post_url = argv[1]
    email = {'email': argv[2]}

    email = parse.urlencode(email).encode('utf-8')
    req = request.Request(post_url, email)

    with request.urlopen(req) as resp:
        resp = resp.read()
        resp = resp.decode('utf-8')
        print(resp)
