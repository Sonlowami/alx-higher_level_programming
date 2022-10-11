#!/usr/bin/python3
class Square:
    """Define a square"""
    def __init__(self, size=0, position=(0, 0)):

        """Initialize the size of the square, raises TypeError
        if size is not an int
        Args:
            size: the size of the square"""
        self.size = size
        self.__position = position

    def area(self):
        """Compute the area of the square
        Return: the area of the square"""

        return self.__size**2

    @property
    def position(self):
        """Return the tuple whose value is in protected value position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set/change the value of the variable in position
        Args:
            value: the value of the position field; it must be a tuple
        Raise:
            TypeError - if the variable is not tuple
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
            self.__position = value

    @property
    def size(self):
        """Return the value stored in variable size"""
        return self.__size

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
        while i < self.size:
            j, x = 0, 0
            while x < self.position[0]:
                print(" ", end="")
                x += 1

            while j < self.size:
                print("#", end="")
                j += 1
            print("")
            i += 1

        if self.__size == 0:
            print("")
