#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight_sum = 0
    Average = 0
    for tuples in my_list:
        score, weight = tuples
        Average += score * weight
        weight_sum += weight
    return Average / weight_sum
