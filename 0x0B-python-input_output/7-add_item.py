#!/usr/bin/python3

"""
Module 9-add_item

Contains function that adds and saves to Python obj to JSON file; loads objects

"""


from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

f = "add_item.json"

try:
    listing = load_from_json_file(f)
except FileNotFoundError:
    listing = []

save_to_json_file(listing + argv[1:], f)
