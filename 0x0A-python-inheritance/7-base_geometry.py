#!/usr/bin/python3
"""Contain a class BaseGeometry"""


class BaseGeometry:
    """Create an abstract class BaseGeometry"""

    def area(self):
        """create an abstract instance method area"""
        raise Exception("Area() is not implimented")

    def integer_validator(self, name, value):
        """Validate if an value is an accepted integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
