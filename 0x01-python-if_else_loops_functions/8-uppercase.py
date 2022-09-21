#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) > 96 and ord(ch) < 123:
            print("{:c}".format(chr(ord(ch) - 32)), end='')
        else:
            print(f"{ch}", end='')
    print("\n")
