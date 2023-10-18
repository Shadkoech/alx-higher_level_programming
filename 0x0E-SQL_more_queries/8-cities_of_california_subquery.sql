-- Script listing all the cities of California from the database hbtn_0d_usa.-- states table has one record name = California
-- Output in ascending order by cities.id

SELECT id, name
 FROM cities
 WHERE state_id IN
	(SELECT id
	  FROM states
	  WHERE name = "California")
 ORDER BY id;
