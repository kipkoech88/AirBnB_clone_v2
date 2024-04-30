-- Build the initia Mysql database for AirBnB project
-- It creates a database if it doesnt exists
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- create a user if doesnt exists
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant privileges to hbnb_dev on performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
