#!/usr/bin/python3
""""Test the base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test different functionalities of the base class"""

    def test_id(self):
        """Test the value of id"""
        base = Base()
        base1 = Base(12)
        base2 = Base("16")
        base3 = Base()
        self.assertEqual(base.id, 1)
        self.assertEqual(base1.id, 12)
        self.assertEqual(base2.id, "16")
        self.assertEqual(base3.id, 2)

    def test_to_json_string(self):
        """Test to_json_string function"""
        self.assertEqual([], '[]')
        self.assertEqual([{1}], '[{1}]')
        self.assertEqual([{'Name': "me"}], "[{name: me}]")
        self.assertEqual([None], '[]')
        self.assertEqual([{'lang': 'python'}, {'learner': 'Uwimana', 'school': 'ALX'}], '[{lang: python}, {learner: Uwimana, school = ALX}]')


if __name__ == '__main__':
    unittest.main()
