#!/usr/bin/python3

"""
Module 6-load_from_json_file

Write a function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """ load json file """
    import json
    with open(filename, "r", encoding="UTF8") as f:
        return json.load(f)
