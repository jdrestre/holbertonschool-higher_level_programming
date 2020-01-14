#!/usr/bin/python3
"""Define rectangle Class
"""


class Rectangle:
    """Is a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes rectangle features"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """instance attribute width"""
        return self.__width

    @property
    def height(self):
        """instance attribute height"""
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
