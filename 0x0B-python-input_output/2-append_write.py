#!/usr/bin/python3
"""Contain only a method to append to a file"""


def append_write(filename="", text=""):
    """Append text to a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
