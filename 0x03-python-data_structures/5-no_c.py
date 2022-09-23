#!/usr/bin/python3
def no_c(my_string):
    lmy_string = list(my_string)
    for ch in lmy_string:
        if ch == 'c' or ch == 'C':
            lmy_string.remove(ch)
    my_string = ''.join(str(item) for item in lmy_string)
    return my_string
