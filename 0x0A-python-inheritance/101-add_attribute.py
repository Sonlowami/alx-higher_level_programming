#!/usr/bin/python3
"""Contain a function that adds an attribute to an object if possible"""


def add_attribute(obj, key, value):
    """Attempt to add an attribute to an object"""
    try:
        vars(obj)[key] = value
    except Exception:
        raise TypeError("can't add new attribute")
