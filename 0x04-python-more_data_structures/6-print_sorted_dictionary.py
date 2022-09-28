#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for skey in sorted(a_dictionary):
        print("{}: {}".format(skey, a_dictionary[skey]))
