#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# check if the number is negative or not
if number < 0:
    lastDigit = number % -10  # get the last digit
else:
    lastDigit = number % 10
# check the conditions
if lastDigit == 0:
    print("Last digit of {} is {} and is 0".format(number, lastDigit))
elif lastDigit > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, lastDigit))
elif lastDigit < 6:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, lastDigit))
