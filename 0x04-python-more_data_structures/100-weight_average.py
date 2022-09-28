#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) > 0:
        sm, weight = 0, 0
        for tp in my_list:
            if type(tp) is tuple:
                sm += tp[0] * tp[1]
                weight += tp[1]
        return sm / weight
    return 0
