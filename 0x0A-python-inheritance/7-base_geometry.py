#!/usr/bin/python3
"""
module with class BaseGeometry
"""


class BaseGeometry:
    """a BaseGeometry class"""

    def area(self):
        """method for calculating area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a function to validate if a num is integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
