#!/usr/bin/python3
"""Contain a class Student"""


class Student:
    """Define objects of type student"""

    def __init__(self, first_name, last_name, age):
        """Initialize the attributes of a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of student objects"""
        if not attrs:
            return self.__dict__

        res = {}
        for string in attrs:
            if type(string) is str:
                try:
                    res[string] = self.__dict__[string]
                except Exception:
                    pass
        return res

    def reload_from_json(self, json):
        """Read attributes of object from file"""
        self.__dict__ = json
