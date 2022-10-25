#!/usr/bin/python3
"""Contain a class Student"""


class Student:
    """Define objects of type student"""

    def __init__(self, first_name, last_name, age):
        """Initialize the attributes of a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of student objects"""
        return self.__dict__
