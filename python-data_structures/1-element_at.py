#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < length and idx >= 0:
        return(my_list[idx])
    else:
        return(None)
