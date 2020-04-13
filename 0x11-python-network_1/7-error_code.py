#!/usr/bin/python3
"""
Docstrig
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    try:
        r = requests.get(argv[1])
        print(r.text)
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(r.status_code))
