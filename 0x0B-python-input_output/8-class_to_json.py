#!/usr/bin/python3
""" a class_to_json module"""


def class_to_json(obj):
    """a function that returns the dictionary description with simple data
    structure(list, dictionary, string, integer and boolean)"""
    return obj.__dict__
