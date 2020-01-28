#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Task 2: create a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Task 2: initializate rectangle"""

        """Task 2: private instance attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Task 2 assign each arguments to right attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Task 3: add TypeError and ValueError execption"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Task 2 assign each arguments to right attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Task 4: Return area Rectangle"""
        return self.width * self.height

    def display(self):
        """Task 5: Diplay print Rectangle instance with #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print(" ", end="") for w in range(self.width)]
            print("")
