#!/usr/bin/python3
"""Module containing class Rectangle"""


class Rectangle:
    """Contain instances and methods pertaining to rectangles"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize private instance variables for width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles
        Return: the biggest rectangle, rect_1 if they have same size"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of type rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

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
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.width != 0 and self.height != 0:
            return 2 * (self.height + self.width)
        else:
            return 0

    def __str__(self):
        """Return a string representation of a rectangle"""
        recta = ""
        unit = 0
        while unit < self.height:
            wid = 0
            while wid < self.width:
                recta += Rectangle.print_symbol
                wid += 1
            if unit < self.height - 1:
                recta += "\n"
            unit += 1
        return recta

    def __repr__(self):
        """Return the official string representation of a rectangle
        This can be used to recreate it"""

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Detect object deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
