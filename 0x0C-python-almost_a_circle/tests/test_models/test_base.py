#!/usr/bin/python3
""""Test the base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test different functionalities of the base class"""

    def setUp(self):
        """Initialize objects"""
        self.a = Base()
        self.b = Base()
        self.c = Base(12)
        self.d = Base()

    def test_id(self):
        """Test the value of id"""
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 2)
        self.assertEqual(self.c.id, 12)
        self.assertEqual(self.d.id, 3)

if __name__ == '__main__':
    unittest.main()
