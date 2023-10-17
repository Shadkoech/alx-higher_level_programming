-- SQL script that lists the number of records having the same score from the table second_table from the hbtn_0c_0 database
-- Result should display the score and number of record for this score having the label number
-- Number of records should be descending

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
