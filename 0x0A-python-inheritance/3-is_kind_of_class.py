#!/usr/bin/python3
"""compare object is an instance of a class that inherited
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
