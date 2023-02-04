#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return(0)
    result = 0
    prev = 0
    for char in roman_string[::-1]:
        curr_value = roman[char]
        if prev > curr_value:
            result -= curr_value
        else:
            result += curr_value
        prev = curr_value
    return (result)
