#!/usr/bin/python3
""" a read_file module"""
def read_file(filename=""):
    """function that reads a text file and prints it"""

    with open(filename) as f:
        file = f.read()
        print(file, end="")
