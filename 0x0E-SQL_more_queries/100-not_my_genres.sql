-- SQL script listing all shows and all genres linked to the show
-- If shows does have a genre, NULL is diplayed
-- Every record displays 

SELECT DISTINCT name
  FROM tv_genres AS g
  INNER JOIN tv_show_genres AS s
  ON g.id = s.genre_id

  INNER JOIN tv_shows AS t
  ON s.show_id = t.id
  WHERE g.name NOT IN
	(SELECT name
		FROM tv_genres AS g
		INNER JOIN tv_show_genres AS s
		ON g.id = s.genre_id

		INNER JOIN tv_shows AS t
		ON s.show_id  = t.id
		WHERE t.title = "Dexter")
  ORDER BY g.name
