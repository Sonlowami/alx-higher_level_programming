-- Show all ratings for every show
SELECT title, SUM(rate) AS rating 
	FROM tv_shows 
	INNER JOIN tv_show_ratings 
	ON tv_show_ratings.show_id = tv_shows.id 
	GROUP BY title 
	ORDER BY rating 
	DESC;
