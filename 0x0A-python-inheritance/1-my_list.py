#!/usr/bin/python3
""" print_sorted module """


class MyList(list):
    """
    MyList class
    """

    def print_sorted(self):
        """a function that prints MyList lists in ascending order by value.
        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
