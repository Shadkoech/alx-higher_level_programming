-- Script that lists all cities in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Output is sorted in ascending order by cities.id

SELECT c.id, c.name, s.name
FROM cities as c
INNER JOIN states AS s
ON c.states_id = s.id
ORDER BY c.id ASC;
