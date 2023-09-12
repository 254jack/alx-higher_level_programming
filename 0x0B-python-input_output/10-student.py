#!/usr/bin/python3
"""
Student module
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method for retrieve a dictionary representation for a
        student instance"""

        if attrs is None:
            return self.__dict__
        dict = {}
        for key, value in self.__dict__.items():
            for i in attrs:
                if key == i:
                    dict[key] = value
        return dict
