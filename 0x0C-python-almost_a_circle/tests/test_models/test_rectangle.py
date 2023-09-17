#!/usr/bin/python3
"""Testcase module for the class Rectangle"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Testcases for the class Rectangle"""

    def setUp(self):
        """method that prepares the test fixture. Called before any
        test methods"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Checks the assignment of class id. if not passed it should
        be assigned using nb logic. If assigned, return the assigned
        value"""

        r1 = Rectangle(5, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(5, 7)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(1, 6)
        self.assertEqual(r3.id, 3)
        r4 = Rectangle(5, 8, 4, 7, 20)
        self.assertEqual(r4.id, 20)
        r5 = Rectangle(7, 16, 22, 4, 13)
        self.assertEqual(r5.id, 13)

    def test_attr(self):
        """apart from id, this test covers the rest of the rectangle
        attributes that include width, height, x and y in that
        order"""

        r1 = Rectangle(4, 8)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(7, 8, 12, 15)
        self.assertEqual(r2.width, 7)
        self.assertEqual(r2.height, 8)
        self.assertEqual(r2.x, 12)
        self.assertEqual(r2.y, 15)

    def test_inheritance(self):
        """This test checks the inheritance process from class Base"""

        r1 = Rectangle(4, 8)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_instance(self):
        """checks object/instance of a class"""
        r1 = Rectangle(15, 8)
        r2 = Rectangle(11, 9)
        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(type(Rectangle) == type(Base))
        self.assertTrue(type(r1) == type(r2))
        self.assertFalse(id(r1) == id(r2))

    def test_error_raise(self):
        """checks the module response when errors occur"""

        with self.assertRaises(TypeError) as cm:
            r = Rectangle("Python", 7)
        self.assertEqual("width must be an integer", str(cm.exception))

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(10, "Python")
        self.assertEqual("height must be an integer", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            r = Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            r = Rectangle(7, 0)
        self.assertEqual("height must be > 0", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            r = Rectangle(5, 8, -4, 7)
        self.assertEqual("x must be >= 0", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            r = Rectangle(5, 8, 4, -7)
        self.assertEqual("y must be >= 0", str(cm.exception))

    def test_area(self):
        """Method that validates the area of the rectangle"""
        r1 = Rectangle(4, 8)
        self.assertEqual(r1.area(), 32)

        r2 = Rectangle(3, 5, 2, 0)
        self.assertEqual(r2.area(), 15)

    def test_area_error(self):
        """checking out the error on area"""
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(5)
            r1.area()
        self.assertEqual("__init__() missing 1 required positional argument: 'height'", str(cm.exception))

    # def test_display(self):
        """Method that checks how the rectangle is displayed in the
        stdout"""


    def test_str(self):
        """method that checks the str representation"""
        r1 = Rectangle(7, 5, 3, 8, 19)
        self.assertEqual(str(r1), "[Rectangle] (19) 3/8 - 7/5")

        r2 = Rectangle(4, 5, 9)
        self.assertEqual(str(r2), "[Rectangle] (1) 9/0 - 4/5")

        r3 = Rectangle(3, 8)
        self.assertEqual(str(r3), "[Rectangle] (2) 0/0 - 3/8")












if __name__ == '__main__':
    unittest.main()
