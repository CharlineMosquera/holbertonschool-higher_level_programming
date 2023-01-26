#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = sys.argv
    len = len(args)
    if len == 1:
        print("{} arguments.".format(len - 1))
    elif len == 2:
        print("{} argument:".format(len - 1))
        print("{}: {}".format(len - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(len - 1))
        i = 1
        while i < len:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
