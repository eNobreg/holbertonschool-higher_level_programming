-- Select city and states
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.idi ORDER BY cities.id ASC;