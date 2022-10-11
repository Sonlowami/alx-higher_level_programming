#!/usr/bin/python3
class Square:
    """Define a square"""
    def __init__(self, size=0):
        
        """Initialize the size of the square, raises TypeError
        if size is not an int
        Args:
            size: the size of the square"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Compute the area of the square
        Return: the area of the square"""

        return self.__size**2
    
    @property
    def size(self):
        """Return the value stored in variable size"""
        return self.__size + 0

    @size.setter
    def size(self, value):
        """change the value stored in private variable size
        Args:
            value: new value of size
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
