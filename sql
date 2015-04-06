CREATE DATABASE profdb CHARACTER SET utf8;
CREATE USER prof@localhost IDENTIFIED BY 'prof';
GRANT ALL PRIVILEGES ON profdb.* TO prof@localhost;