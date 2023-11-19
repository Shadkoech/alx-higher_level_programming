# 0x0F. Python - Object-relational mapping

This project orchestrates the very first linked between a Database and Python code. It occurs in two steps:

1. The use of the module MySQLdb to connect to a MySQL database in order to execute SQL queries.
2. The application of SQLAlchemy as an Object Relational Mapper (ORM).

## Setting up working environment

### Installation and activation of venv

For this project, a Python Virtual Environment (venv) was set up by installing venv for the following reasons:

	- Isolation and Dependency Management since venv ensure that packages and dependencies installed for this project does not interfere with other projects
	- Portability ensuring that required dependencies can be easily installed on different systems when the project is shared.
	- System protection by avoiding scenarios where packages installed into Python's global environment can lead to conflicts with existing tools.

The following commands were run to create the venv:

* $ sudo apt-get install python3.8-venv
* $ python3 -m venv venv
* $ source venv/bin/activate


### Installion of MySQLdb module version 2.0.3

Having installed MySQL in my Ubuntu 20.04 system, MysQLdb was installed into the venv using the commands:

* $ sudo apt-get install python3-dev
* $ sudo apt-get install libmysqlclient-dev
* $ sudo apt-get install zlib1g-dev
* $ sudo pip3 install mysqlclient
...


### Install SQLAlchemy module version 1.4.22

Inside the venv;

* $ sudo pip3 install SQLAlchemy
...




This folder (0x0F. Python - Object-relational mapping) contains a number of individual projects done in the set environment above that practice a number of SQLAlchemy ORM functionalities as follows:

## Task 0: Get all states

File:

	- 0-select_states.py
A script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id



## Task 1: Filter states

File:

	- 1-filter_states.py
A script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
Build on the previous task;



## Task 2: Filter states by user input

File:

	- 2-my_filter_states.py
Python script that builds on the previous (1-filter_states.py) and  takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id



## Task 3: SQL Injection...

File:

	- 3-my_safe_filter_states.py
A python script same as 2-my_filter_states.py but this time safe from MySQL injections



## Task 4: Cities by states

File:

	- 4-cities_by_state.py
Write a script that lists all cities from the database hbtn_0e_4_usa. Builds from the previous 3-my_safe_filter_states.py but can only be executed once



## Task 5: All cities by state

File:

	- 5-filter_cities.py
 a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
Results must be sorted in ascending order by cities.id
You can use only execute() once



## Task 6: First state model

File:

	- model_state.py
a python file that contains the class definition of a State and an instance Base = declarative_base():

State class:
* inherits from Base Tips
* links to the MySQL table states
* class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
* class attribute name that represents a column of a string with maximum 128 characters and can’t be null
* You must use the module SQLAlchemy
* Your script should connect to a MySQL server running on localhost at port 3306



## Task 7: All states via SQLAlchemy

File:

	- 7-model_state_fetch_all.py
A script that lists all State objects from the database hbtn_0e_6_usa
* Results must be sorted in ascending order by states.id



## Task 8: First state

File:

	- 8-model_state_fetch_first.py
A script that prints the first State object from the database hbtn_0e_6_usa
* The state you display must be the first in states.id
* You are not allowed to fetch all states from the database before displaying the result
* If the table states is empty, print Nothing followed by a new line



## Task 9: Contains `a`

File:

	- 9-model_state_filter_a.py
A script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
* Results must be sorted in ascending order by states.id



## Task 10: Get a state

File:

	- 10-model_state_my_get.py
A script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
* Results must display the states.id
* If no state has the name you searched for, display Not found



## Task 11:  Add a new state

File: 

	- 11-model_state_insert.py
A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
* Print the new states.id after creation




## Task 12: Update a state

File:

	- 12-model_state_update_id_2.py
A script that changes the name of a State object from the database hbtn_0e_6_usa
* Change the name of the State where id = 2 to New Mexico



## Task 13: Delete states

File:

	- 13-model_state_delete_a.py
A script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
* You must import State and Base from model_state - from model_state import Base, State



## Task 14: Cities in state

Files: 

	- model_city.py, 14-model_city_fetch_by_state.py

Python file similar to model_state.py named model_city.py that contains the class definition of a City.

City class:

* inherits from Base (imported from model_state)
* links to the MySQL table cities
* class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
* class attribute name that represents a column of a string of 128 characters and can’t be null
* class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id
* You must use the module SQLAlchemy

Next, write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:

* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by cities.id
* Results must be display as they are in the example below (<state name>: (<city id>) <city name>)
* Your code should not be executed when imported
