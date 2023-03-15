#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                  "D": 500, "M": 1000}
    numric = 0
    last_digit = 0
    for i in roman_string[::-1]:
        numric_value = roman_dict[i]
        if numric_value >= last_digit:
            numric += numric_value
            last_digit = numric_value
        else:
            numric -= numric_value
    return numric
