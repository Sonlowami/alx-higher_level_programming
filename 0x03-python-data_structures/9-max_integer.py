#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = my_list[0]
    for i in my_list:
        if i > maximum:
            maximum = i
    return maximum
