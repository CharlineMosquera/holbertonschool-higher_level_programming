#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list.copy()
    if idx >= len(my_list) or idx < 0:
        return(newlist)
    else:
        newlist[idx] = element
        return(newlist)
