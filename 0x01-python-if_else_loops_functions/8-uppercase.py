#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        asc_ch = ord(ch)

        if asc_ch in range(97, 123):
            asc_ch -= 32

        print("{:c}".format(asc_ch), end="")
    print()
