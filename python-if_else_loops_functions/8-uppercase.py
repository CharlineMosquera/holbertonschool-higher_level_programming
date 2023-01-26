#!/usr/bin/python3
def uppercase(str):
    i = ""
    for letter in str:
        if ord(letter) in range(97, 123):
            result = ord(letter) - 32
            i += chr(result)
        else:
            result = letter
            i += result
    print("{}".format(i))
