#!/usr/bin/python3
""" print_sorted module """


class MyList(list):
    """ a class Myclass that inherits from list"""

    def print_sorted(self):
        """ a function that prints the sorted list"""
        print(sorted(self))
