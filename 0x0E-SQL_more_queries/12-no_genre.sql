-- Script that lists all the shows in hbtn_0d_tvshows database
-- Record should display tv_shows.title - tv_show_genres.genre_id
-- Sort output in ascending order by v_shows.title and tv_show_genres.genre_id


SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
WHERE g.genre_id IS NULL
ORDER BY s.title, g.genre_id 
