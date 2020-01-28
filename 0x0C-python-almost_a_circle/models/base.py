#!/usr/bin/python3
"""define a base model class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Task 15: return Json serialization of list dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Task 16: write json serialization of list of objects to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Task 17: return deseriatlization of json string"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)
