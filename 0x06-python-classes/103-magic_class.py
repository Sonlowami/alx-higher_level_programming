#!/usr/bin/python3
"""The module containing a re-engineered class"""
import math


class MagicClass:
    """MagicClass - a class purely reconstructed from bytecode"""

    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Calculate the area of the circle"""
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """Calculate the circumference of a circle"""
        return math.pi * 2 * self.__radius
