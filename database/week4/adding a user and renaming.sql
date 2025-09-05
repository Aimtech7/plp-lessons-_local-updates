-- create a new user
CREATE USER aim2@localhost
IDENTIFIED BY '7031';
-- VERYFY
SELECT user
FROM mysql.user;
-- change a user password
ALTER USER aim2@localhost
IDENTIFIED BY '2025';

-- RENAME A USER
RENAME USER 
aim2@localhost TO aimtech@localhost;

-- verify
SELECT user
FROM mysql.user;