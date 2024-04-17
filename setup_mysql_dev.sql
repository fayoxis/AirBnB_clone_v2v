-- Prepare MySQL server for project

-- Database, user and password variables
SET @database = 'hbnb_dev_db';
SET @user = 'hbnb_dev';
SET @password = 'hbnb_dev_pwd';

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS @database; 

-- Create user if not exists  
CREATE USER IF NOT EXISTS @user IDENTIFIED BY @password;

-- Grant privileges to user
GRANT ALL PRIVILEGES ON @database.* TO @user;
GRANT SELECT ON performance_schema.* TO @user;

-- Apply privileges  
FLUSH PRIVILEGES;
