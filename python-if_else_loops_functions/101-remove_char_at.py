#!/usr/bin/python3
import sys
def remove_char_at(str, n):
    length = len(str)
    copy = ""
    for letter in str:
        if n <= length:
            if letter != str[n] and n >= 0:
                copy += letter
            elif n < 0:
                copy += letter
        else:
            copy += letter
    return(copy)
