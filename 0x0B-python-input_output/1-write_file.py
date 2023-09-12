#!/usr/bin/python3

""" a write_file module"""


def write_file(filename="", text=""):
    """  a function that writes a string to a text file
    and returns the number of characters written"""

    with open(filename, encoding="utf-8") as f:
        char = f.write(text)
        return (char)
