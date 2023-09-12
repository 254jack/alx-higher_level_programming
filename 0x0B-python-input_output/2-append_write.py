#!/usr/bin/python3
"""an append_write module"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file and returns
    the number of characters added
    """
    with open(filename, "a+")as f:
        char = f.write(text)
        return (char)
