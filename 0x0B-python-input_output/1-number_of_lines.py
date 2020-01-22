#!/usr/bin7python3
"""function that returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    """return number lines of file
    """
    with open(filename, encoding='utf-8') as myFile:
        return len(myFile.readlines())
