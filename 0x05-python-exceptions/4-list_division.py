#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_new_list = []
    try:
        for i in range(list_length):
            try:
                my_new_list.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                my_new_list.append(0)
                print("division by 0")
            except TypeError:
                my_new_list.append(0)
                print("wrong type")
            except IndexError:
                my_new_list.append(0)
                print("out of range")
    finally:
        return my_new_list
