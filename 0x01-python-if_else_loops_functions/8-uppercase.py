#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) > 96 and ord(ch) < 123:
            a = ord(ch) - 32
        else:
            a = ord(ch)
        print("{}".format(chr(a)), end='')
    print("")
