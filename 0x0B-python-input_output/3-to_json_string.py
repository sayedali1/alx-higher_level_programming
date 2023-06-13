#!/usr/bin/python3

"""
Module 3-to_json_string

function that returns the JSON representation
"""


def to_json_string(my_obj):
    """ encoding """
    import json
    return(json.dumps(my_obj))
