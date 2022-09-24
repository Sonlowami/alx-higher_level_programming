#!/usr/bin/python3
def remove_char_at(strn, n):
    if n < len(strn) and n >= 0:
        copy = strn[0:n] + strn[n + 1:]
        return copy
    return strn
