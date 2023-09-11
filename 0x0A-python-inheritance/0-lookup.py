#!/usr/bin/python3
""" a module with method lookup"""


def lookup(obj):
    """ a function that returns a list of available attributes
    and methods inside a class"""
    return dir(obj)
