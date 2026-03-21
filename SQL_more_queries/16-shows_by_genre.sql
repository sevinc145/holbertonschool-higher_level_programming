-- List shows and genres
-- select with many conditions
SELECT s.title, g.name FROM tv_shows s
LEFT JOIN tv_show_genres t ON s.id = t.show_id
LEFT JOIN tv_genres g ON g.id = t.genre_id
ORDER BY s.title ASC, g.name ASC;
