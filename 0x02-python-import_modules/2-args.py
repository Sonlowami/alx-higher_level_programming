#!/usr/bin/python3
from sys import argv
i = 1
num = len(argv) - 1
if __name__ == '__main__':
    if num == 1:
        print("{} argument:".format(num))
    elif num == 0:
        print("{} arguments.".format(num))
    else:
        print("{} arguments:".format(num))
    while i < len(argv):
        print("{} : {}".format(i, argv[i]))
        i += 1
