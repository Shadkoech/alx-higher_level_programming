-- script that lists all the shows that are contained in the database hbtn_0d_tvshows
-- Every record must have the tv_shows.title - tv_show_genres.genre_id
-- Output sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT s.title, g.genre_id
FROM tv_shows AS s
INNER JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title ASC AND g.genre_id ASC
