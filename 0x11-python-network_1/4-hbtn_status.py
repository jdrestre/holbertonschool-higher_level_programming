#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status.
"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html.decode('utf8'))))
        print('\t- content: {}'.format(html.decode('utf8')))
