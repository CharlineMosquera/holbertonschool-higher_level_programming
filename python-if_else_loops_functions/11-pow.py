#!/usr/bin/python3
def pow(a, b):
    i = 0
    result = 1
    while i < abs(b):
        result = a * result
        i += 1
    if b < 0:
        result = 1 / result
    return(result)
