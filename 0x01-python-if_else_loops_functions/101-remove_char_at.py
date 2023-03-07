#!/usr/bin/python3
def remove_char_at(str, n):
    j = 0
    s2 = ""
    for ch in str:
        if j != n:
            s2 = s2 + ch

        j += 1

    return s2
