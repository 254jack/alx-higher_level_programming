#!/usr/bin/python3
""" Finding a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    """ Find a peak using binary search """

    if not list_of_integers:
        return None

    lw, hi = 0, len(list_of_integers) - 1

    while lw < hi:
        mid = (lw + hi) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            hi = mid
        else:
            lw = mid + 1

    return list_of_integers[lw]
