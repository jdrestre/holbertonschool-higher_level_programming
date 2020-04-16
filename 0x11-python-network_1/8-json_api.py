#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable `q`
If no argument is given, set `q=""`
"""
import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    r = requests.post(url, data={'q': letter})
    try:
        response = r.json()
        if len(response) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
    except ValueError:
        print('Not a valid JSON')
