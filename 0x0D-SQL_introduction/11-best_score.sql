-- SQL script listing all the records having a score of >= 10 in the second_table of the database hbtn_0c_0
-- Output should contain both score and name 
-- Records ordered by the score

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
