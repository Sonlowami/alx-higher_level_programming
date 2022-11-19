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

    def test_setters_with_2_numbers(self):
        """Test setter functions with positive and negative numbers"""
        rect = Rectangle(45, 5)

        self.assertEqual(rect.width, 45)
        self.assertEqual(rect.height, 5)

    def test_setters_with_3_numbers(self):
        """Test setters with three numbers"""
        rect = Rectangle(45, 5, 1)

        self.assertEqual(rect.width, 45)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 0)

    def test_setters_with_4_numbers(self):
        """Test with width, height, x and y"""
        rect = Rectangle(45, 5, 1, 8)

        self.assertEqual(rect.width, 45)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 8)
    
    def test_width_setter1(self):
        """Test width setter with negative value"""
        with self.assertRaises(ValueError):
            rect = Rectangle(-67, 2, 44, 4)

    def test_height_setter1(self):
        """Test height setter with negative value"""
        with self.assertRaises(ValueError):
            rect = Rectangle(67, -2, 44, 4)

    def test_x_setter1(self):
        """Test x setter with negative value"""
        with self.assertRaises(ValueError):
            rect = Rectangle(67, 2, -44, 4)

    def test_y_setter1(self):
        """Test y setter with negative value"""
        with self.assertRaises(ValueError):
            rect = Rectangle(67, 2, 44, -4)

    def test_width_float(self):
        """Test setter functions with a float"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3.14, 4)

    def test_height_float(self):
        """Test height setter functions with a float"""
        with self.assertRaises(TypeError):
            rect = Rectangle(4, 4.2)

    def test_x_float(self):
        """Test x setter functions with strings"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 4, 5.3)

    def test_y_float(self):
        """Test y setter functions with strings"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, 4, 5, 1.3)

    def test_width_setter2(self):
        """Try to set width and height to 0"""
        with self.assertRaises(ValueError):
            a = Rectangle(0, 2)

    def test_height_setter2(self):
        with self.assertRaises(ValueError):
            a = Rectangle(2, 0)

    def test_area(self):
        rect = self.rect
        self.assertEqual(rect.area(), 90)
        rect.height = 10
        self.assertEqual(rect.area(), 20)
