#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is".format(number), end=" ")
# check if the number is negative or not
if number < 0:
    lastDigit = number % -10  # get the last digit
else:
    lastDigit = number % 10
# check the conditions
if lastDigit == 0:
    print(f"{lastDigit:d} and is 0")
elif lastDigit > 5:
    print(f"{lastDigit:d} and is greater than 5")
elif lastDigit < 6:
    print(f"{lastDigit:d} and is less than 6 and not 0")
