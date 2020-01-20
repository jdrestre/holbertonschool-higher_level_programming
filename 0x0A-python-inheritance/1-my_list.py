#!/usr/bin/python3
"""class MyList that inherits from list
"""


class MyList(list):
    """Class MyList inherits from list"""
    def print_sorted(self):
        """list sorted"""
        print(sorted(self))
        """
        print("{}".format(sorted(self)))
        """
