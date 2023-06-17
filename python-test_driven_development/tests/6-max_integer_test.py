#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test class"""
    def test_max_integer(self):
        test_list = []
        self.assertEqual(max_integer(test_list), None)
        test_list = [1, 3, 5]
        self.assertEqual(max_integer(test_list), 5)
        test_list = [1, 6, 5]
        self.assertEqual(max_integer(test_list), 6)
        test_list = [6, 2, 1]
        self.assertEqual(max_integer(test_list), 6)
        test_list = [2, -5, 6, 0]
        self.assertEqual(max_integer(test_list), 6)
        test_list = [-9, -3, -6]
        self.assertEqual(max_integer(test_list), -3)
        test_list = [1]
        self.assertEqual(max_integer(test_list), 1)

if __name__ == '__main__':
    unittest.main()
