#!/usr/bin/python3
"""Return a seriarizable dictionary representation of an object"""


def class_to_json(obj):
    """Return a seriarizable dictionary"""
    return vars(obj)
