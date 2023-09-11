#!/usr/bin/python3
"""
Builds on the previously created empty class BaseGeometry by adding
    A public instance method def area(self)
    public instance method: def integer_validator(self, name, value):
Returns:
    class with an public instance method
"""


class BaseGeometry:
    """
    Adding up public instance method area
    """
    def area(self):
        """
        Method that calculates the area of the Geometric class
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
