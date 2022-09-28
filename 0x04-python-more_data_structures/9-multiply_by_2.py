#!/usr/bin/python
def multiply_by_2(a_dictionary):
    dc = {}
    for k, v in a_dictionary.items():
        dc[k] = v * 2
    return dc
