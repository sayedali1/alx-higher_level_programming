#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not idx < 0 or idx > len(my_list):
        my_list.remove(my_list[idx])
        new_list = my_list.copy()
    return new_list
