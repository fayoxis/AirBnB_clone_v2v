-- This script sets up a MySQL server for a project
-- Create the project development database with the name 'hbnb_dev_db'
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user named 'hbnb_dev' with all privileges on the 'hbnb_dev_db' database
-- The password for this user is 'hbnb_dev_pwd' if the user doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the 'hbnb_dev_db' database to the user 'hbnb_dev'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- Grant the SELECT privilege to the user 'hbnb_dev' on the 'performance_schema' database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
