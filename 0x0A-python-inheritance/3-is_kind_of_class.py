#!/usr/bin/python3
"""Contain a function to check isinstance"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or any of it's ancestors"""
    return isinstance(obj, a_class)
