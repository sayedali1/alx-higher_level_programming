#!/usr/bin/python3
"""
Module 8-class_to_json
Contains function that
returns dictionary description with simple data structure

"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure
    Args:
        obj: python object
    """
    return obj.__dict__
