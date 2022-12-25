#!/usr/bin/python3
"""Test safe_print_list
    
    >>> safe_print_list([], x = 0)
    >>>
    >>> safe_print_list([4], x = 0)
    4
    >>> safe_print_list([4, 6], x = 1)
    6
    >>> safe_print_list([4, 6, 8], x = 2)
    8
    >>> safe_print_list([4, 6, 8, "None"], x = 3)
    None
    >>>
    """
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            print(str(my_list[i]), end="")
            i += 1
    except IndexError:
        pass
    print("")
    return i

if __name__=='__main__':
    import doctest
    doctest.testmod()
