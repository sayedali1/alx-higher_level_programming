#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    bigNum = my_list[0]
    for i in my_list:
        if bigNum < i:
            bigNum = i
    return bigNum
