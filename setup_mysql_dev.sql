-- This script sets up a MySQL server for a project

-- Create the project development database if it doesn't exist
DROP DATABASE IF EXISTS hbnb_dev_db;
CREATE DATABASE hbnb_dev_db;

-- Create a new user 'hbnb_dev' with the password 'hbnb_dev_pwd' if it doesn't exist
-- Grant all privileges on the 'hbnb_dev_db' database to this user
DROP USER IF EXISTS 'hbnb_dev'@'localhost';
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- Grant the SELECT privilege to the user 'hbnb_dev' on the 'performance_schema' database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
