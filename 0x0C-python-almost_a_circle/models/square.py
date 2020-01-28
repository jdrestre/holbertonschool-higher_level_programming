#!/usr/bin/python3
"""Define square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represent square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize new square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    def __str__(self):
        """Return print and str representation square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
