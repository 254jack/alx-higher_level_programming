#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    w_sum = 0
    product = 0

    for i in my_list:
        product += i[0] * i[1]
        w_sum += i[1]
    result = product / w_sum

    return result
