# BCS-Quiz-Manager

# DataBase
This project uses a PSQL Database, this will need to be installed prior to running the code.

## To create the DB:
`sudo su - postgres`\
`psql`\
`CREATE DATABASE quizdb;`\
`CREATE USER quizdb WITH PASSWORD 'password';`\
`GRANT ALL PRIVILEGES ON DATABASE quizdb TO quizdb;`\
`\q`

## To run the project localy:
Clone the repository to your local machine \
Create a virtual environment using the virtual environment of your choice \
Activate your virtual environment and install the project requirements using \
`pip install -r requirements.txt`

Create a superuser:
`python manage.py create_superuser`

###
Start the application using \
`python manage.py runserver` \
The appliction can then be accessed via: localhost:8000 \
Access the admin page using the path /admin/
If this is the first time running the project, you will need to create some user groups to manage the permissions. 
Log in to http://localhost:8000/admin/auth/group/ and add a group for Edit, Restricted & View
An Edit user can have all permissions
A View user should have can_view_answers & can_view_questions
A Restricted user should have can_view_questions
