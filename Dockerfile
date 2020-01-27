FROM postgres:latest

# RUN mkdir /docker-entrypoint-initdb.d/
COPY init-user-db.sh /docker-entrypoint-initdb.d/init-user-db.sh
