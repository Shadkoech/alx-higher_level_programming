-- Script using hbtn_0d_tvshows database to list all the genres of show Dexter
-- Shows table contain one record where title = Dexter
-- Each record must display tv_genres.name
-- Output ascending by genre name

SELECT g.name
 FROM tv_genres AS g
	INNER JOIN tv_show_genres AS s
	ON g.id = s.genre_id

	INNER JOIN tv_shows AS t
	ON t.id = s.show_id
	WHERE t.title = "Dexter"
 ORDER BY g.name;
