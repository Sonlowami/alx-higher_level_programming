-- Show all genres that 'Dexter' show belongs to
SELECT name FROM tv_shows
	INNER JOIN tv_show_genres
	ON tv_show_genres.show_id = tv_shows.id
	INNER JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
	WHERE title LIKE 'Dexter'
	ORDER BY name;
