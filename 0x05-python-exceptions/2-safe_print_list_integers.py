#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{:d}".format(int(my_list[i])), end="")
        except TypeError:
            pass
        except ValueError:
            pass
        i += 1
    print("")
    return i