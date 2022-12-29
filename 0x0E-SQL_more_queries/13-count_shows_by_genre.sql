-- Show all  genres and the number of tv shows
SELECT name AS genre, COUNT(show_id) AS number_of_shows
	FROM tv_show_genres
	RIGHT JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
	GROUP BY genre
	ORDER BY number_of_shows DESC;
