#!/usr/bin/python3
"""Contain the class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Create a class square that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize instance attributes of class square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of a square"""
        return f"[Square] ({self.id}), {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Return the value of width"""
        return self.width

    @size.setter
    def size(self, value):
        """Change the value of width and height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.width, self.height = value, value

    def update(self, *args, **kwargs):
        """Update attributes of a square"""
        if args and len(args) != 0:
            try:
                self.id = args[0]
                self.width, self.height = args[1], args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                elif key == 'id':
                    self.id = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

        def to_dictionary(self):
            """Return a dictionary representation of a square"""
            return self.__dict__
