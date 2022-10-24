#!/usr/bin/python3
"""Contain only a function to check if an object is
    an instance of a class"""


def is_same_class(obj, a_class):
    """Check if an object is of precisely a specific type"""
    if type(obj) is a_class:
        return True
    return False
