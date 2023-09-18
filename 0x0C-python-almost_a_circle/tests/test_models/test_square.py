#!/usr/bin/python3
"""Module that handles Tests cases for the class square"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestClassSquare(unittest.TestCase):
    """Testcase methods to test the class square"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instance(self):
        """testing the class instances and inheritance
        of class Square"""
        s1 = Square(7)
        self.assertIsInstance(s1, Square)
        self.assertTrue(issubclass(Square, Rectangle))
        s2 = Square(5)
        self.assertTrue(type(s1) == type(s2))
        self.assertFalse(id(s1) == id(s2))

    def test_attributes(self):
        """Validating the different square attributes"""

        s1 = Square(5)
        self.assertEqual(s1.id, 1)

        s2 = Square(8, 7, 1)
        self.assertEqual(s2.width, 8)
        self.assertEqual(s2.height, 8)
        self.assertEqual(s2.x, 7)
        self.assertEqual(s2.y, 1)
        self.assertEqual(s2.id, 2)

    def test_errors(self):
        """Testing out error based on inheritance"""

        with self.assertRaises(ValueError):
            s1 = Square(0)
        with self.assertRaises(ValueError):
            s2 = Square(1, 7, -3, 8)
        with self.assertRaises(ValueError):
            s3 = Square(-5)
        with self.assertRaises(TypeError):
            s4 = Square(7, "4", 8)
        with self.assertRaises(NameError):
            s5 = square_self(6)

    def test_setters(self):
        """checking errors thrown on setters"""
        s1 = Square(5)

        with self.assertRaises(ValueError):
            s1.x = -7
        with self.assertRaises(ValueError):
            s1.y = -4
        with self.assertRaises(ValueError):
            s1.size = -6
        with self.assertRaises(TypeError):
            s1.size = "6"
        with self.assertRaises(TypeError):
            s1.x = "7"

    def test_update(self):
        """testing out the **kwargs in the updated method"""

        s1 = Square(5)
        s1.update(12)
        self.assertEqual(s1.id, 12)
        s1.update(x=15)
        self.assertEqual(s1.x, 15)
        s1.update(size=11, id=3, x=8, y=9)
        self.assertEqual(s1.size, 11)
        self.assertEqual(s1.id, 3)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 9)

    def test_dictionary(self):
        """Testing out the dictionary representation of the square"""

        s1 = Square(7, 3, 8)
        s1_dictionary = s1.to_dictionary()
        test_dictionary = {'x': 3, 'y': 8, 'id': 1, 'size': 7}
        self.assertEqual(len(s1_dictionary), len(test_dictionary))

    def test_area(self):
        """Checking the area method of the square"""

        s1 = Square(6, 2)
        self.assertEqual(s1.area(), 36)
        s2 = Square(15, 20, 4, 50)
        self.assertEqual(s2.area(), 225)
        s3 = Square(20)
        self.assertEqual(s3.area(), 400)

    def test_string(self):
        """testing the string representation of the square"""

        s1 = Square(9, 7, 3, 8)
        self.assertEqual(str(s1), "[Square] (8) 7/3 - 9")
        s2 = Square(4, 2, 3)
        self.assertEqual(str(s2), "[Square] (1) 2/3 - 4")


if __name__ == "__main__":
    unittest.main()
