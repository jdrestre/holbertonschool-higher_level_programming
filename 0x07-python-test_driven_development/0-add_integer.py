#!/Usr/bin/python3
""" Doc """


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

"""
def add_integer(a, b=98):
    """ """
    if a != a:
        a = 89
    if b != b:
        b = 89
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
"""


"""add_integer function that adds 2 integers


def add_integer(a, b=98):
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not float and type(b) is not int:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
"""
