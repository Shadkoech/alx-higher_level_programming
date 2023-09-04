#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by:
    - Private instance attribute width
    - Private instance attribute height
    - public instance method that calculates the area
    - Use of __str__() method to print rectangle with char #
    - Use of repr() to return a string representation of the
    rectangle to be able to create a new instance by eval()
    - Application of the del() function to delete a rectangle
    - creation of a public attribute (number_of_instances)
    - Another public class attribute (print_symbol)
    - Use of a static method def bigger_or_equal(rect_1, rect_2)
The width and height must be integers otherwise
Raises:
    TypeError: width must be an integer
    TypeError: height must be an integer
"""


class Rectangle:
    """Class definition called Rectangle with privately set
    width and height attributes
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """computes area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        "computes the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """prints the rectangle with character #"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            symbol = str(self.print_symbol)
            return "\n".join([symbol * self.width] * self.height)

    def __repr__(self):
        """return a string representation of the object with format
        "Rectangle(width, height)". It is therefore possible to create
        Rectangle with same attr using eval"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """a destructor of equal measure"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
