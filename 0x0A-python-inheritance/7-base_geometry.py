#!/usr/bin/python3
"""create empty class BaseGeometry
"""


class BaseGeometry():
    """ Task 6: Class BaseGeometry with Exception
    """
    def area(self):
        """not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Task 7: public instance validate value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
