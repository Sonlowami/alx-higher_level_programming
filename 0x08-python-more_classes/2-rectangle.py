#!/usr/bin/python3
"""Module containing class Rectangle"""


class Rectangle:
    """Contain instances and methods pertaining to rectangles"""

    def __init__(self, width=0, height=0):
        """Initialize private instance variables for width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Access the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Access the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set or change the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @width.setter
    def width(self, value):
        """Set or change the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """Return the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width != 0 and self.__height != 0:
            return 2 * (self.__height + self.__width)
        else:
            return 0
