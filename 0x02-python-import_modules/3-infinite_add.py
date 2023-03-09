#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 1:
        sum = 0
        for index, argv in enumerate(sys.argv[1:], 1):
            if index == 1:
                sum = int(argv)
            else:
                sum = sum + int(argv)
        print(sum)
