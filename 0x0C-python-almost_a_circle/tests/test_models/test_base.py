#!/usr/bin/python3
"""Unittest module for base.py"""

import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestClassBase(unittest.TestCase):
    """class definition that will be used to develop test-cases for
    the file base.py"""

    def setUp(self):
        """Testing framework method that automatically calls for every
        test carried out"""
        Base._Base__nb_objects = 0

    def test_object_creation(self):
        """testing object types and id"""
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertNotEqual(b1, Base())
        self.assertNotEqual(id(b1), id(Base()))

        b2 = Base()
        self.assertEqual(type(b1), type(b2))
        self.assertNotEqual(id(b1), id(b2))

    def test_new_instances(self):
        """checking id assignment of new class objects"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(22)
        self.assertEqual(b3.id, 22)

    def test_unique_id(self):
        """test for random unique object id"""
        self.assertEqual(21, Base(21).id)

    def test_json(self):
        """Test on static method that return Json str representation"""

        r1 = Rectangle(1, 7, 3, 8)
        dictionary = (r1.to_dictionary())
        json_dictionary = Base.to_json_string(sorted(dictionary.items()))
        self.assertEqual(json_dictionary, '[["height", 7], ["id", 1], '
                         '["width", 1], ["x", 3], ["y", 8]]')

        dictionary = []
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json_dictionary, '[]')


if __name__ == "__main__":
    unittest.main()
