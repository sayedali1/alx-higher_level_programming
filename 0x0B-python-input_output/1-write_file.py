#!/usr/bin/python3
"""
Module 1-write_file

function that writes a string to a text file
"""


def append_write(filename="", text=""):
    with open(filename, mode="w", encoding="UTF8") as f:
        return(f.write(text))
