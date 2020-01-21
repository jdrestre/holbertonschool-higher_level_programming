#!/usr/bin/python3
"""create classe square inherits in rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square based to Rectangle
    """
    def __init__(self, size):
        """initialize instance size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """print area
        """
        return self.__size * self.__size
