#!/usr/bin/python3
def new_in_list(my_list, idx, element):
        list_2 = my_list[:]
        if idx > 0 and idx < len(list_2):
            list_2[idx] = element
        return list_2
