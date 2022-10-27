#!/usr/bin/python3
"""Add whitespaces in a text"""


def text_indentation(text):
    """Add 2 new lines after characters '.', '?', '!'"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    i = 0
    while i < len(text):
        if text[i] not in ['.', '?', '!']:
            print('{}'.format(text[i]), end="")
        else:
            print("\n\n", end="")
            if i < len(text) - 1 and text[i + 1].isspace():
                i += 1
        i += 1
