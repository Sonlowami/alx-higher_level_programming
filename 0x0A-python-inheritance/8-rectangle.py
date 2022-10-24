#!/usr/bin/python3
"""Contain Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Define properties of a rectangle"""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
