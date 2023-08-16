#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    d_keys = list(a_dictionary.keys())
    d_keys.sort()
    for key in d_keys:
        print("{}: {}".format(key, a_dictionary.get(key)))
