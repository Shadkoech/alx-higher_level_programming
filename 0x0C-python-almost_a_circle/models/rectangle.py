#!/usr/bin/python3
""" A module of class rectangle that inherits from Class Base"""

from models.base import Base


class Rectangle(Base):
    """Defining a class Rectangle which is a subclass to Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter to the triangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the triangle width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """privatizing and getting the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getting the triangle's x-coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the triangle's x-coordinate"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """privatizing and getting y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the triangles's y coordinate"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method that calculates the area of a rectangle"""
        return (self.width * self.height)

    def display(self):
        """Method that prints rectangle instance using character #"""
        for i in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """updating the class Rectangle by overriding the __str__method
        in order to return [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Method that assigns an argument to every other attribute"""
        # the key thing to note is that *args packs arguments in a tuple
        # that means the arguments can be indexed
        if args:
            for i in range(len(args)):
                if i == 0:
                    if not isinstance(args[i], int):
                        raise TypeError("id must be an integer")
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    if not isinstance(value, int):
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
