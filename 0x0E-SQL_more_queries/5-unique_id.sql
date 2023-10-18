-- SQL script that creates a table called unique_id on the MySQL server
-- Table fields: id INT with the default value 1 and must be unique, name VARCHAR(256)
-- Script shouldn't fail if the table exist

CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
