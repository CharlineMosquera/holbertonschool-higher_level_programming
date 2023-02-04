#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for element in range(x):
            print(my_list[element], end="")
    except IndexError:
        return(element)
    else:
        return(x)
    finally:
        print("")
