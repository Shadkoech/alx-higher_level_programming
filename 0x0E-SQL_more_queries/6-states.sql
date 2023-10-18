-- Script creating hbtn_0d_usa and table states in the database
-- states table fields: id INT unique, auto generated, can’t be null and is a primary key, name VARCHAR(256) can’t be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256));
