#!/usr/bin/python3
"""
Docstrig
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/user"
    user = argv[1]
    password = argv[2]
    
    r = requests.post(url, headers={'Authorization': 'token {}'.format(password)})
    print(r.json().get('id'))
