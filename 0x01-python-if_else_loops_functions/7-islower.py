#!/usr/bin/python3

def islower(c):
    asc_c = ord(c)

    if asc_c in range(97, 123):
        return True
    else:
        return False
