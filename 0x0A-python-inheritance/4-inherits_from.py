#!/usr/bin/python3
"""Contain a method to check if an object is ot type subclass"""


def inherits_from(obj, a_class):
    """Check if ob is an instance of a subclass of a_class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
