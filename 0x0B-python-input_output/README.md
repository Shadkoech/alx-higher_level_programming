## 0x0B. Python - Input/Output
This directory contains various concepts on how python handles text and binary files in terms of opening them, reading, writing into files, appending, closing files etc. Through the help of question and tasks the following key questions finds answers:
	* How do you open a file
	* How to read, write or append a file
	* How to read the full content of a file
	* How do you ensure that a file is closed after using it
	* What is and how to use the 'with' statement
	* What is JSON
	* What is serialization and deserialization

### Task 0: Read file
	- def read_file(filename=""): - function that reads a textfile and prints it out to the stdout

### Task 1: Write to a file
	- def write_file(filename="", text=""): - A function that writes to a string to a text file and returns the number of characters written

### Task 2: Append to a file
	- def append_write(filename="", text=""): - Function used to appends a string at the end of a text file and return the number of character added

### Task 3: To JSON string
	- def to_json_string(my_obj): - A function that returns the JSON's representation of a string

### Task 4: From JSON string to Object
	- def from_json_string(my_str):- Function use to return the python representation of JSON's string

### Task 5: Save Object to a file
	- def save_to_json_file(my_obj, filename): A function that writes an object to a text file using JSON representation

### Task 6: Create object from a JSON file
	- def load_from_json_file(filename): - A function that creates an object from JSON file

### Task 7: Load, add, save
	- Script written that add all arguments to a python list and then saves them to a given file

### Task 8: Class to JSON
	- def class_to_json(obj): - This is a function that returns the dictionary description with simple data structures such as list, dictionary, string, integer and boolean for JSON serialization of agiven object

### Task 9: Student to JSON
	- Creation of a class Student that defines student by public attributes of first_name, last_name and age

### Task 10: Student to JSON with filter
	- A build up on the class Student through the addition of public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance

### Task 11: Student to disk and reload
	- More build-up on the class by adding another public instance method def reload_from_json(self, json): that replaces all attributes of the Student instance

### Task 12: Pascal's Triangle
	- def pascal_triangle(n): - A function tha returns a list of integers representing the Pascal's triangle of n
