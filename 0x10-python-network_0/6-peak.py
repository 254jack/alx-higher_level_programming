#!/usr/bin/python3
""" finding peak in a list of integers
"""


def find_peak(list_of_integers):
    """
    a find peak method
    """
    pik = None
    for i in list_of_integers:
        if pik is None or pik < i:
            pik = i
    return pik
