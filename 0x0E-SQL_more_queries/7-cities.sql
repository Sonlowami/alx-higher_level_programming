-- Create a table cities with reference to state ID
-- Create database in case it's not created already
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(ID)
	);

