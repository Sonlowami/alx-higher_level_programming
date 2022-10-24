#!/usr/bin/python3
"""Contain a function that adds an attribute to an object if possible"""


def add_attribute(obj, key, value):
    """Attempt to add an attribute to an object"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    vars(obj)[key] = value
