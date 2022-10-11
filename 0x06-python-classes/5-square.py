#!/usr/bin/python3
class Square:
    """Define a square"""
    def __init__(self, size=0):

        """Initialize the size of the square, raises TypeError
        if size is not an int
        Args:
            size: the size of the square"""
        self.size = size

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

    def my_print(self):
        """Print the square out using '#'"""
        i = 0
        while i < self.__size:
            j = 0
            while j < self.__size:
                print("#", end="")
                j += 1
            print("")
            i += 1
        if self.__size == 0:
            print("")
