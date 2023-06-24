
CREATE DATABASE microservice;

GRANT ALL PRIVILEGES ON DATABASE blog TO blog;
GRANT ALL PRIVILEGES ON DATABASE microservice TO blog;

ALTER ROLE blog SET client_encoding TO 'utf8';
ALTER ROLE blog SET default_transaction_isolation TO 'read committed';
ALTER ROLE blog SET timezone TO 'UTC';