#!/usr/bin7python3
"""function that returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    """return number lines of file
    """
    num_lines = 0
    with open(filename) as myFile:
        for line in myFile:
            num_lines += 1
    return num_lines
