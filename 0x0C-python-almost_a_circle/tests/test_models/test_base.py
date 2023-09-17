#!/usr/bin/python3
"""Unittest module for base.py"""

import unittest

from models.base import Base


class TestclassBase(unittest.TestCase):
    """class definition that will be used to develop test-cases for
    the file base.py"""

    def object_creation(self):
        obj1 = Base()
        self.assertIsInstance(obj1, Base)
        self.assertFalse(type(obj1) == type(Base))
        self.assertFalse(id(obj1) == id(Base))

        obj2 = Base()
        self.assertFalse(id(obj1) == id(obj2))
        self.assertTrue(type(obj1) == type(obj2))

    def unique_id(self):
        self.assertEqual(21, Base(21).id)


if __name__ == "__main__":
    unittest.main()
