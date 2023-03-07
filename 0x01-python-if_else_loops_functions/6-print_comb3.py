#!/usr/bin/python3

spliter = ", "  # spilt each two digits

for i in range(0, 10):  # range of the first digit
    for j in range(i + 1, 10):  # range of the sec digit
        if i == j or i > j:  # check if the same two digit
            continue        # or digits has been printed
        else:
            if i == 8:  # change the spilter for the last line
                spliter = "\n"
            print("{:d}{:d}".format(i, j), end=spliter)
