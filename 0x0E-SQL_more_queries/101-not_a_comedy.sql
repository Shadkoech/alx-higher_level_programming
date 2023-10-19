-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- tv_genres table has one record where name = Comedy
-- Each record should display: tv_shows.title

SELECT title
FROM tv_shows
WHERE id NOT IN(
	SELECT DISTINCT s.id
	FROM tv_shows AS s
	JOIN tv_show_genres AS g ON s.id = g.show_id
	JOIN tv_genres AS g ON s.genre_id = g.id
	WHERE g.name = "Comedy")
 ORDER BY title ASC;

