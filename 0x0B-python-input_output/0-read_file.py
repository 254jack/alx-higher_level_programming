#!/usr/bin/python3
""" a read_file module"""


def read_file(filename=""):
    """ a function that reads a text file and prints it to stdout"""
    with open("UTF8", "r") as f:
        file = f.read()
        print(file, end="")
