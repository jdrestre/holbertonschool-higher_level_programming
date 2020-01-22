#!/usr/bin/python3
"""creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """load objects from json file
    """
    with open(filename, "r", encoding='utf-8') as myFile:
        return json.load(myFile)
