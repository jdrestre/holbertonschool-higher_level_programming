#!/usr/bin/python3
"""define number of lines of a text file
"""


def number_of_lines(filename=""):
    """return number of lines
    """
    lines = 0
    with open(filename, "r", encoding='utf-8') as myFile:
        for line in myFile:
            lines += 1
    return lines
