#!/usr/bin/python3
"""
Docstrig
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    email = {'email': argv[2]}
    r = requests.post(argv[1], data=email)
    print(r.text)