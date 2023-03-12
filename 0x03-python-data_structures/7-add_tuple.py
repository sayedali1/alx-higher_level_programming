#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_list = [list(tuples) for tuples in [tuple_a, tuple_b]]
    for supList in new_list:
        while len(supList) < 2:
            supList.append(0)
        while len(supList) > 2:
            supList.pop()
    a0, a1 = new_list[0]
    b0, b1 = new_list[1]
    new_list = [a0 + b0, a1 + b1]

    return tuple(new_list)
