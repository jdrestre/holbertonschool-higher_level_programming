#!/usr/bin/python3
"""Define rectangle Class
Task 0 is Empty class
"""


class Rectangle:
    """Task 6: Initialize Public Class Attribute Number of Instance"""
    number_of_instances = 0

    """Task 1: Is a Rectangle"""
    def __init__(self, width=0, height=0):
        """Task 6: add Incremented during each new instance instantiation"""
        type(self).number_of_instances += 1
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
        """property to set it width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """property to set it height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Task 2: public instance method that returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method: that returns rectangle perimeter:"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Task 3: return printable rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        """algorithm to print rectangle with #"""
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Task 4: Return string representation rectangle to be able to recreate
        a new instance using eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Task 6: Decremented during each instance deletion"""
        type(self).number_of_instances -= 1
        """Task 5: instance of Rectangle is deleted"""
        print("Bye rectangle...")
