-- Find all cities of California
SELECT cities.id, cities.name FROM cities INNER JOIN states WHERE cities.state_id = states.id;
