#!/usr/bin/python3

"""
Module 5-save_to_json_file

function that writes an Object to a text file
"""


def save_to_json_file(my_obj, filename):
    import json
    with open(filename, "w", encoding="UTF8") as f:
        f.write(json.dumps(my_obj))
