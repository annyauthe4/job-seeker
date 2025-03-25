-- Set a database for the Job seeker project
-- Create user, database and grant privileges

-- Create a Database job_dev_db if it does not exists
CREATE DATABASE IF NOT EXISTS job_dev_db;

-- Create user job_dev if it does not exist
CREATE USER IF NOT EXISTS 'job_dev'@'localhost' IDENTIFIED BY 'job_dev_pwd';

-- Grant all privileges on the job_dev_dbdatabase to job_dev user
GRANT ALL PRIVILEGES ON job_dev_db.* TO 'job_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'job_dev'@'localhost';

FLUSH PRIVILEGES;
