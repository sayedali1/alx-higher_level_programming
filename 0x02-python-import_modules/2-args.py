#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    index = 0
    for i in sys.argv:
        if index == 0:
            index += 1
            continue
        print("{:d}: {}".format(index, i))
        index += 1
