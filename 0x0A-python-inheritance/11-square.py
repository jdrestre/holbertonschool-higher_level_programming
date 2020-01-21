#!/usr/bin/python3
"""create classe square inherits in rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent Square based to Rectangle
    """
    def __init__(self, size):
        """square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """print details square instance
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
