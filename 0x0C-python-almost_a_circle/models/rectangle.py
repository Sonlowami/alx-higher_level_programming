#!/usr/bin/python3
"""Create a rectangle that inherits from the base class"""
from models.base import Base


class Rectangle(Base):
    """The rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize attributes of a rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gives access to a private attribute"""
        return self.__width

    @property
    def height(self):
        """Gives access to a private attribute height"""
        return self.__height

    @property
    def x(self):
        """Gives access to a private attribute x"""
        return self.__x

    @property
    def y(self):
        """Gives access to a private attribute y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """set the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """set the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """Print a rectangle out"""

        self.__print_whitespace(self.y, '\n')
        i = self.y
        while i < self.y + self.height:
            self.__print_whitespace(self.x, " ")
            j = self.x
            while j < self.x + self.width:
                print("#", end='')
                j += 1
            print("")
            i += 1

    def __print_whitespace(self, times, char):
        """Print whitespace character n times"""
        i = 0
        while i < times:
            print(char, end='')
            i += 1

    def __str__(self):
        """"Return a string representation of a rectangle"""
        return f"[rectangle] ({self.id}) {self.x}/{self.y} -\
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update the attributes of a rectangle"""
        if not args or len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "height":
                    self.height = value
                elif key == "width":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == 'y':
                    self.y = value
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """return a dictionary representation of a rectangle"""
        return self.__dict__
