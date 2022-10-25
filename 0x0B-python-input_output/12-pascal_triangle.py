#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Create a pascal's triangle of n length"""
    return_list, inter_list = [], []
    i = 0
    if n <= 0:
        return None
    if n > 0:
        return_list = [[1]]
        i += 1
    if n > 1:
        return_list.append([1, 1])
        inter_list = [1, 1]
        i += 1
    while i < n:
        lst = [1]
        j = 0
        while j < len(inter_list):
            if j < len(inter_list) - 1:
                lst.append(inter_list[j] + inter_list[j + 1])
            j += 1
        lst.append(1)
        return_list.append(lst)
        inter_list = lst
        i += 1
    return return_list
