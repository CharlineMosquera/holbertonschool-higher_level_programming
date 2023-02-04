#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = [replace if i == search else i for i in my_list]
    return (newlist)
