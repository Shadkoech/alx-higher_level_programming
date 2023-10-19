-- SQL script that lists all the shows from hbtn_0d_tvshows_rate by their rating.
-- Every show should display tv_shows.title - rating sum
-- Output sorted in descending order

SELECT t.title, SUM(rate) AS rating
  FROM tv_shows AS t
  INNER JOIN tv_show_ratings AS r
  ON t.id = r.show_id
ORDER BY rating DESC;
