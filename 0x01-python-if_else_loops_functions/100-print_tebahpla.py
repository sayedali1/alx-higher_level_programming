#!/usr/bin/python3
upper = False   # chage from upper to lower
for i in range(90, 64, -1):  # walk back word
    if not upper:
        i += 32
        upper = True
    else:
        upper = False
    print("{:c}".format(i), end="")
