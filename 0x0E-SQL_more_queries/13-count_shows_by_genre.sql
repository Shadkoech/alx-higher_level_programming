-- Script listing all genres from the htbn_0d_tvshows database from Mysql server
-- Every record must show <TV Show genre> - <Number of shows linked to this genre>
-- First column is  genre
-- Second column is number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Output in descending order by the number of shows linked


SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_shows_genre AS t
ON g.id = t.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC
