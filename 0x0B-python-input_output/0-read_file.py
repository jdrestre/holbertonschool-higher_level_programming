#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end='')
