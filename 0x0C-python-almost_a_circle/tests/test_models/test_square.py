#!/usr/bin/python3
""""Test the base class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test attributes of a square"""

    def setUp(self):
        """Create code that executes before every test function"""
        self.square = Square(1, 1, 1, 1)

    def test_properties(self):
        """Test properties"""
        self.assertEqual(self.square.size, 1)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 1)

    def test_setters_with_numbers(self):
        """Test setters with positive and negative numbers"""

        self.square.size = 4
        self.square.x = 0
        self.square.y = 0
        self.assertEqual(self.square.size, 4)
        self.assertEqual(self.square.x, 0)
        self.assertEqual(self.square.y, 0)

        self.assertRaises(TypeError, self.square.size, -1)
        self.assertRaises(TypeError, self.square.x, -1)
        self.assertRaises(TypeError, self.square.y, -1)

    def test_setters_with_strings_and_floats(self):
        """Test with strings and floats"""

        self.assertRaises(TypeError, self.square.size, 2.4)
        self.assertRaises(TypeError, self.square.x, 2.5)
        self.assertRaises(TypeError, self.square.y, 3.0)
        self.assertRaises(TypeError, self.square.size, "3.1)")
        self.assertRaises(TypeError, self.square.x, "3.3")
        self.assertRaises(TypeError, self.square.y, "3.6")

    def test_setters_with_none(self):
        """Test setters with None value"""

        self.assertRaises(TypeError, self.square.size, None)
        self.assertRaises(TypeError, self.square.y, None)
        self.assertRaises(TypeError, self.square.y, None)
