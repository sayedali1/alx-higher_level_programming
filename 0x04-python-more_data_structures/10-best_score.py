#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for key in a_dictionary.keys():
            if a_dictionary[key] == sorted(a_dictionary.values())[-1]:
                return key
    else:
        return None
