#!/usr/bin/python3
"""function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is', first_name, last_name)

"""
def say_my_name(first_name, last_name=""):
    """"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My Name is", first_name, last_name)
"""
"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My Name is {} {}".format(first_name, last_name))
"""
