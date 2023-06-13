#!/usr/bin/python3

"""
Module 2-append_write

function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """ append text on file """
    with open(filename, mode="a", encoding="UTF8") as f:
        return(f.write(text))
