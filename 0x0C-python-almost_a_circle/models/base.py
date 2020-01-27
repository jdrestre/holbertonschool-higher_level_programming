#!/usr/bin/python3
"""define a base model class"""


class Base:
    """Represent base model"""

    __nb_objects = 0
    """atribut: number of instantiated Bases"""

    def __init__(self, id=None):
        """init new Base - Argument: id(int)"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
