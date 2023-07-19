-- script that lists all cities contained in the database 
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
WHERE cities.id = states.id
ORDER BY cities.id ASC;
