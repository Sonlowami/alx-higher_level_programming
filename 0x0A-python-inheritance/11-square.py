#!/usr/bin/python3
"""Contain a  class square that defines attributes of type square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Create a class Square"""

    def __init__(self, size):
        """initialize a square"""
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size
        self.__size = size

    def area(self):
        """Calculate the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation"""
        return f"[Square] {self.__size}/{self.__size}"
