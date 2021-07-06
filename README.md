# BCS-Quiz-Manager

DataBase
This project uses a PSQL Database, this will need to be installed prior to running the code.

To create the DB:
sudo su - postgres
psql
CREATE DATABASE quizdb;
CREATE USER quizdb WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE quizdb TO quizdb;
\q