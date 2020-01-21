#!/usr/bin/python3
"""adds a new attribute to an object
"""


def add_attribute(obj, att, val):
    """add attribute if is possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
