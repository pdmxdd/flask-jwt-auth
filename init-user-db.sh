#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER db_user WITH ENCRYPTED PASSWORD 'dbpass';
    CREATE DATABASE db;
    GRANT ALL PRIVILEGES ON DATABASE db TO db_user;

    CREATE USER db_test_user WITH ENCRYPTED PASSWORD 'dbpass';
    CREATE DATABASE db_test;
    GRANT ALL PRIVILEGES ON DATABASE db_test TO db_test_user;
EOSQL
