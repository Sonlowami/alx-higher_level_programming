#!/usr/bin/python3
"""Contain a function that will print a square"""


def print_square(size):
    """print a square"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    i = 0
    while i < size:
        j = 0
        while j < size:
            print('#', end="")
            j += 1
        i += 1
        print("")
