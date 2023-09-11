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
        Raises:
            Exception: "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value
        Args:
            name (str): name of value in question
            value(in): actual value to be validated
        Raises:
            TypeError: if value is not int
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
