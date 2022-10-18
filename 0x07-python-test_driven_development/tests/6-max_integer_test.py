#!/usr/bin/python3
"""Test max_integer function"""
max_integer = __import__('6-max_integer').max_integer
import unittest


class TestMaxInteger(unittest.TestCase):
    """Test defining test methods"""
    
    def test_wrong(self):
        """Tests for the wrong input"""
        self.assertRaises(TypeError, max_integer, "Never mind")
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(ValueError, maxInteger, ['1', 'None', 3])

    def test_list(self):
        self.assertEqual(max_integer([1]), 1)
        self.assertIs(max_integer(), None)
        self.assertEqual(max_integer([1, 4, 3, -8]), 4)
        self.assertEqual(max_integer([-4, -7]), -4)


if __name__=='__main__':
    unittest.main()
