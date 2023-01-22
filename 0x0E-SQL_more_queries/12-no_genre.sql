-- Show all tv shows that have no genre linked
SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE genre_id IS NULL
ORDER BY title, genre_id;
