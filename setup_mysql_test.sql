-- This script sets up a MySQL server for testing purposes

-- Create the project testing database if it doesn't exist
DROP DATABASE IF EXISTS hbnb_test_db;
CREATE DATABASE hbnb_test_db;

-- Create a new user 'hbnb_test' with the password 'hbnb_test_pwd' if it doesn't exist
-- Grant the SELECT privilege on the 'performance_schema' database to this user
DROP USER IF EXISTS 'hbnb_test'@'localhost';
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- Grant all privileges on the 'hbnb_test_db' database to the user 'hbnb_test'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
