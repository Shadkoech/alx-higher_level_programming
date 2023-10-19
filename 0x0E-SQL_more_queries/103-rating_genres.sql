-- SQL script listing all shows without the genre Comedy
-- tv_genres table contains only one record where name = Comedy
-- Every record should display: tv_shows.title
-- Output sorted in ascending order by the show title

SELECT name, SUM(tv_show_ratings.rate) 'rating'
FROM tv_genres AS g
INNER JOIN tv_show_genres AS s ON g.id = s.genre_id
INNER JOIN tv_show_ratings AS r ON s.show_id = r.show_id
GROUP BY name
ORDER BY rating DESC;
