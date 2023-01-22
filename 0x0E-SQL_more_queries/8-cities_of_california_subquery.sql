-- Find all cities of California
SELECT cities.id, cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name LIKE 'California' ORDER BY cities.id;
