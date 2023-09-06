#!/usr/bin/python3
"""
unittest for max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_max_integer(self):
        """gets max int from unordered list"""
        unordered = [5, 2, 7, 3, 1]
        self.assertEqual(max_integer(unordered), 7)

    def test_max_int_ordered(self):
        """gets max integer from ordered list"""
        ordered = [1, 3, 6, 9, 15]
        self.assertEqual(max_integer(ordered), 15)

    def text_max_negative(self):
        """gets max even from a list with negatives"""
        neg_list = [5, 4, -6, -15, 8, -10]
        self.assertEqual(max_integer(neg_list), 8)

    def test_empty(self):
        """tries to get max value from an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_max_beg(self):
        """gets max value at beginning of list"""
        max_beginning = [15, 5, -8, 9, 3]
        self.assertEqual(max_integer(max_beginning), 15)

    def only_negatives(self):
        """gets a maximum value from a list of negative numbers"""
        negative_list = [-5, -7, -15, -30, - 18]
        self.assertEqual(max_integer(negative_list), -5)

    def test_one_element(self):
        """checks a list of one element"""
        one_list = [5]
        self.assertEqual(max_integer(one_list), 5)

    def test_floats(self):
        """gets max from floats and its"""
        float = [1.8, 17.55, 2, 9, 22.30, 15]
        self.assertEqual(max_integer(float), 22.30)


if __name__ == '__main__':
    unittest.main()
