-- Prepare MySQL server for project

-- Define database, user and password
DEFINE db_name = 'hbnb_dev_db';
DEFINE user_name = 'hbnb_dev';   
DEFINE password = 'hbnb_dev_pwd';

-- Create database if not exists
IF NOT EXISTS (SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = db_name)
THEN 
  CREATE DATABASE db_name;
END IF;

-- Create user if not exists   
IF NOT EXISTS (SELECT USER FROM mysql.user WHERE USER = user_name) 
THEN
  CREATE USER user_name IDENTIFIED BY password;
END IF;

-- Grant privileges to user  
GRANT ALL PRIVILEGES ON db_name.* TO user_name;
FLUSH PRIVILEGES;

-- Grant SELECT on performance_schema    
GRANT SELECT ON performance_schema.* TO user_name;
FLUSH PRIVILEGES;
