#!/usr/bin/python3
""" a read_file module"""


def read_file(filename=""):
    """ a function that reads a text file and prints it to stdout
    Args:
    filename (str): name of file to be opened
    """
    with open("UTF8", "r") as f:
        file = f.read()
        print(file, end="")
