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

    def test_setters_with_numbers(self):
        """Test setter functions with positive and negative numbers"""
        rect = self.rect
        """With positive numbers"""
        rect.width = 45
        rect.height = 5
        rect.x = 2
        rect.y = 3

        self.assertEqual(rect.width, 45)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

        """With negative numbers"""

        self.assertRaises(TypeError, self.rect.width, -455)
        self.assertRaises(TypeError, self.rect.height, -5)
        self.assertRaises(TypeError, self.rect.x, -2)
        self.assertRaises(TypeError, rect.y, -3)

    def test_setters_by_strings_and_floats(self):
        """Test setter functions with strings"""

        self.assertRaises(TypeError, self.rect.width, 3.145)
        self.assertRaises(TypeError, self.rect.height, 4.21)
        self.assertRaises(TypeError, self.rect.x, 12)
        self.assertRaises(TypeError, self.rect.y, 0.5)

    def test_area(self):
        rect = self.rect
        self.assertEqual(rect.area(), 90)
        rect.height = 10
        self.assertEqual(rect.area(), 20)
