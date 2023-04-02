#!/usr/bin/python3
"""Find the peak in an unsorted array of numbers"""


def find_peak(list_of_integers):
    """Find the peak of an unsorted array"""

    if len(list_of_integers) == 0 or list_of_integers is None:
        return None
    ints = list_of_integers[:]
    peak = ints[0]
    for num in ints:
        if num > peak:
            peak = num
    return peak
