#!/usr/bin/python3
"""
student module
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a method to covert to json"""
        return self.__dict__
