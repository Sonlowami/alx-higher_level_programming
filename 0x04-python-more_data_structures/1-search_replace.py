#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    dc = {}
    for elem in my_list:
        dc[i] = elem
        i += 1
    for k, v in dc.items():
        if v == search:
            dc[k] = replace
    return list(dc.values())
