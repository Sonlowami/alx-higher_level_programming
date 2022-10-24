#!/usr/bin/python3
"""Contain a class called MyList"""


class MyList(list):
    """Create a class that inherits from list"""

    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
