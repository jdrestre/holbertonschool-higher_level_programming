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
            self.__width = value

        @property
        def height(self):
            """Task 2 assign each arguments to right attribute"""
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value
