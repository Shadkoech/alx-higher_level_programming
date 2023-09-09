#!/usr/bin/python3
"""Python MagicClass from given bytecode"""

import math


class MagicClass:
    """defining the MagicClass that replicates the bytecode"""
    def __init__(self, radius=0):
        """class constructor for the data"""
        self._MagicClass_radius = 0

        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """method finding the area of circle"""
        return math.pi * (self._MagicClass__radius **2)

    def circumference(self):
        """method that calculates the circumference of a circle"""
        return 2 * math.pi * self._MagicClass__radius
