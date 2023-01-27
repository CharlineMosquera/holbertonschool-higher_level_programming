#!/usr/bin/python3
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
    print("{}".format(copy))
