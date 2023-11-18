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


### Installion of MySQLdb module version 2.0.x

Having installed MySQL in my Ubuntu 20.04 system, MysQLdb was installed into the venv using the commands:

* $ sudo apt-get install python3-dev
* $ sudo apt-get install libmysqlclient-dev
* $ sudo apt-get install zlib1g-dev
* $ sudo pip3 install mysqlclient
...
* $ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)


### Install SQLAlchemy module version 1.4.x

Inside the venv;

* $ sudo pip3 install SQLAlchemy
...
* $ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'




This folder (0x0F. Python - Object-relational mapping) contains a number of individual projects done in the set environment above that practice a number of SQLAlchemy ORM functionalities as follows:

## Task 0: Get all states

File:

	- 0-select_states.py
Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id



## Task



## Task



## Task



## Task



## Task



## Task



## Task



## Task



## Task



## Task



## Task



## Task



## Task