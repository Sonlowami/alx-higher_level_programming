#!/usr/bin/python3
"""append after a special line"""


def append_after(filename="", search_string="", new_string=""):
    """A function to append to after every occurance of line in text"""
    buff = ""
    with open(filename, 'r', encoding="utf-8") as f:
        line = f.readline()
        while line != "":
            buff += line
            if search_string in line:
                buff += new_string
            line = f.readline()

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(buff)
