-- SQL script converting a hbtn_0c_0 database to UTF8
-- The database, first_name and name in first_table should all be converted

USE hbtn_0c_0
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8_unicode_ci;
