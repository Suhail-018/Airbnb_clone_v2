-- Prepares a MySQL server.
-- Create hbnb_test_db, user hbnb_test.
-- Grant privileges to the user hbnb_test.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT  ON `performance_schema`.* TO 'hbnb_test'@'localhost';
