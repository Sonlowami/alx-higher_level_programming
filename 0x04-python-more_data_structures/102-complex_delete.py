#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_set = set()
    for k, v in a_dictionary.items():
        if v == value:
            new_set.add(k)
    for k in new_set:
        del a_dictionary[k]
    return a_dictionary
