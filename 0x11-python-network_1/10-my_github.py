#!/usr/bin/python3
"""
Takes in a string and sends a search request to the Star Wars API.
"""
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    r = requests.get(url, auth=(user, password))
    json_repr = r.json()
    print(json_repr.get('id', 'None'))
