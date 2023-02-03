#!/usr/bin/python3
def no_c(my_string):
    str = ''
    for letter in my_string:
        if letter == 'c' or letter == 'C':
            letter
        else:
            str = str + letter
    return(str)
