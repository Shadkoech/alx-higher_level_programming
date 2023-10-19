-- SQL script listing all comedy shows from the database hbtn_0d_tvshows
-- tv_genres table contains only one record where name = Comedy
-- Each record should display: tv_shows.title


SELECT t.title, g.name
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS s
ON t.id = s.show_id

LEFT JOIN tv_genres AS g
ON s.genre_id = g.id
ORDER BY t.title, g.name
