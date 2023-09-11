## 0x0A. Python - Inheritance
This directory contains exercises and tasks on an important aspect of python as OOP which is inheritance. The concept of inheritance allows us to create a hierarchy of classes that actually share a set of properties and methods by deriving a class from its higher class. Some of the key questions answered include:
	* What is a subclass/child/derived class
	* What is a superclass/parent/baseclass for that matter
	* Ways of listing all attributes and methods in a class

	* How to inherit a class from another
	* How to define a class with multiple base classes
	* How to override a method or attribute that is inherited from the base class
	* Purpose and the advantage of inheritance

The tasks handled and the key concept are as follows

### Task 0: Lookup
	- def lookup(obj): - Function used to return a list of available attributes and methods of a given object.

### Task 1: My list
	- def print_sorted(self): - A new child class that inherits from baseclass called list

### Task 2: Exact same object
	- def is_same_class(obj, a_class): - A function that returns True if the object is an instance of specified class and False otherwise

### Task 3: Same class or inherit from
	- def is_kind_of_class(obj, a_class): - Function returning True if onject is an instance of child of parent class and False otherwise

### Task 4: Only sub class of
	- def inherits_from(obj, a_class): - Checks if an object is part of a particular class or a class that the specified class inherited from

### Task 5: Geometry module
	- Writing out an empty class called BaseGeometry

### Task 6: Improve Geometry
	- def area(self): - A method that calculates the area. Raises an exception in the case area cannot be calculated

### Task 7: Integer validator
	- def integer_validator(self, name, value): - Public instance method that validates value. Ensures that it is of type integer and is more than 0

### Task 8: Rectangle
	- Rectangle is a derived class that inherits from BaseGeometry
	- def __init__(self, width, height): - Rectangle method that instatiates height and width

### Task 9: Full rectangle
	- Implements the area method from Base Geometry which is an inherited class
	- Width and height validated by integer validator must be positive integer and private

### Task 10: Square
	- class Square that inherits from class Rectangle
	- def __init__(self, size): - Instatiates the size of the rectangle which must be private


### Task 11: Square #2
	- Buildup of class Square in Task 10 above
	- implements the area method up up from class Geometry

