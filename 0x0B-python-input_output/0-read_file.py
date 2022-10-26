#!/usr/bin/python3
""" Read text from a file and print it"""


def read_file(filename=""):
    """Read text and print it on screen"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
