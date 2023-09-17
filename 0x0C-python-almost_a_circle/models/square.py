#!/usr/bin/python3
"""A module of a new derived class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class square that inherits from class Rectangle which inherits
    from base"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing the class Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of the Square"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """privatizing and getting the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the values of size(width and height)"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """method that assigns square attributes"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    if not isinstance(args[i], int):
                        raise TypeError("id must be an integer")
                    self.id = args[i]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    if not isinstance(value, int):
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Method that represents the class square as
        a dictionary"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
