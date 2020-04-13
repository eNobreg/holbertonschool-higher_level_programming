#!/usr/bin/python3
"""
Docstrig
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        json = r.json()
        if not json:
            print("No result")
        else:
            print('[{}] {}'.format(json['id'], json['name']))
    except ValueError:
            print("Not a valid JSON")
