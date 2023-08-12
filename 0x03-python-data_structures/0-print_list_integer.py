#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list:
        for i in my_list:
            if i in range(48,58):
                print("{}".format(i))
