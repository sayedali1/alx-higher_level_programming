#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if  idx >= 0 and idx < len(my_list):
        my_list.remove(my_list[idx])
        new_list = my_list.copy()
    else:
        return my_list

    return new_list
