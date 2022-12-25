#!/usr/bin/python3
def element_at(my_list, idx):
    """Return the index of a list at position idx

    >>> mylist = [0,1,2,3,4,5]
    >>> element_at(mylist, 3)
    3
    """
    if idx < len(my_list) and idx >= 0:
        return my_list[idx]

if __name__=='__main__':
    import doctest
    doctest.testmod()
