#!/usr/bin/python3
"""
Moduel 0-read_file
fun that read a text
"""


def read_file(filename=""):
    with open(filename, encoding="UTF8") as f:
        print(f.read())
