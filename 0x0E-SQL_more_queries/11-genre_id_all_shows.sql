-- Script listing all shows in the database hbtn_0d_tvshows.
-- Records should output tv_shows.title - tv_show_genres.genre_id
-- Output sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- incase doesn’t have a genre, display NULL

SELECT s.title, g.genre_id
FROM tv_shows As s
LEFT JOIN tv_show_genres As g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
