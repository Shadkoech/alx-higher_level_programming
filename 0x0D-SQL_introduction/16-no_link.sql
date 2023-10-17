-- An SQL script that lists all the records of the second_table
-- Does not list rows lacking name value 
-- Records listed in descending order
-- Rows without names are excluded

SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
