#!/usr/bin/python3
"""object instance of a class that inherited (directlyorindirectly) from class
"""


def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
