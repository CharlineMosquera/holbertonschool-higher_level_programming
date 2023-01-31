#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenght = len(my_list)
    for element in range(my_list[lenght - 1], my_list[0] - 1, -1):
        print("{:d}".format(element))
