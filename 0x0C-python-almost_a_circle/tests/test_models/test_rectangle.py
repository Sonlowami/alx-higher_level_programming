#!/usr/bin/python3
""""Test the base class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test aspects of the rectangle class"""

    def setUp(self):
        self.rect = Rectangle(2, 45, 0, 1, 3)

    def test_properties(self):
        """Test getters of the attributes of a rectangle"""
        rect = self.rect

        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 45)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 1)

    def test_setters_with_positive_numbers(self):
        """Test setter functions with positive and negative numbers"""
        rect = Rectangle(45, 5)

        self.assertEqual(rect.width, 45)
        self.assertEqual(rect.height, 5)
    
    def test_setters_with_negative_numbers(self):
        """With negative numbers"""

        with self.assertRaises(ValueError):
            self.rect.width = -455
        with self.assertRaises(ValueError):
            self.rect.height = -5
        with self.assertRaises(ValueError):
            self.rect.x = -2
        with self.assertRaises(ValueError):
            self.rect.y = -3

    def test_setters_with_floats(self):
        """Test setter functions with strings"""

        self.assertRaises(TypeError, self.rect.width, 3.145)
        self.assertRaises(TypeError, self.rect.height, 4.21)
        self.assertRaises(TypeError, self.rect.x, 12)
        self.assertRaises(TypeError, self.rect.y, 0.5)

    def test_setters_with_zero_a(self):
        """Try to set width and height to 0"""

        with self.assertRaises(ValueError):
            self.a = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            self.a = Rectangle(2, 0)

    def test_setters_with_zero_b(self):
        """Try to set x and y to 0"""

        self.rect.x = 0
        self.rect.y = 0
        self.assertEqual(self.rect.x, 0)
        self.assertEqual(self.rect.y, 0)

    def test_area(self):
        rect = self.rect
        self.assertEqual(rect.area(), 90)
        rect.height = 10
        self.assertEqual(rect.area(), 20)
