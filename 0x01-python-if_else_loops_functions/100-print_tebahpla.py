#!/usr/bin/python3
upper = False
i = 122
while i > 96:
    if upper:
        diff = 32
        upper = False
    else:
        diff = 0
        upper = True
    print("{}".format(chr(i - diff)), end='')
    i -= 1
