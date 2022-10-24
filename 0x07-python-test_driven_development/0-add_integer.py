#!/usr/bin/python3
"""Adding two numbers"""


def add(a, b=98):
    """Add argument A and optional Argument b"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)