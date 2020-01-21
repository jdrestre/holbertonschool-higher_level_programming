#!/usr/bin/python3
"""identify object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ identificate class an object"""
    if type(obj) is a_class:
        return True
    else:
        False
