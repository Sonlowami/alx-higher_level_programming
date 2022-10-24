#!/usr/bin/python3
"""contain a look up function only"""


def lookup(obj):
    """return a list of defined attributes
    args:
        obj: the object to find attributes for
        """
    return dir(obj)
