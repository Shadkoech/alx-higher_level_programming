-- Script that creates MySQL server user user_0d_1
-- The user user_0d_1 gets all priviledges on the MySQL server
-- user_0d_1 passwords set to user_0d_1_pwd
-- Script shouldn't break in the case 

CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL
ON *.*
TO user_0d_1@localhost;
