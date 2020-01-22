#!/usr/bin/python3
"""define Python class for JSON serialization of an object
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    """
    return obj.__dict__
