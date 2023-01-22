-- Show all shows belonging to one or more genres
SELECT tv_shows.title, tv_genres.id AS genre_id
FROM tv_shows INNER JOIN tv_show_genres, tv_genres WHERE tv_show_genres.show_id = tv_shows.id 
AND tv_show_genres.genre_id = tv_genres.id ORDER BY tv_shows.title, tv_genres.id ASC;
