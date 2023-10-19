-- SQL script listing all the commedy shows in the database
-- The tv_genres table has one record where name = Comedy
-- Every record should display: tv_shows.title
-- Output sorted in ascending order by the show title

SELECT t.title
 FROM tv_shows AS t
    INNER JOIN tv_show_genres AS s
    ON t.id = s.show_id

    INNER JOIN tv_genres AS g
    ON g.id = s.genre_id
    WHERE g.name = "Comedy"
 ORDER BY t.title
