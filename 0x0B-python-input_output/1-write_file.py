#!/usr/bin/python3
"""Contain a simple writing method"""


def write_file(filename="", text=""):
    """Write a string into the file and return number of bytes written"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
