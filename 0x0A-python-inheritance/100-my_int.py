#!/usr/bin/python3
"""class MyInt that inherits from int
"""


class MyInt(int):
    """operators inverted
    """
    def __eq__(self, val):
        """operators different
        """
        return self.real != val

    def __ne__(self, val):
        """operator iqual
        """
        return self.real == val
