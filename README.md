# pokemon-backup-api

steps to install and run this django app.
  
  1. Clone this repo into a directory.
  2. Download and Install python from https://www.python.org/downloads/windows/.
  3. Open Command prompt, run "python -m pip install -r requirements.txt".
  3. Install Postgres DB from https://www.postgresql.org/download/windows/.
  4. While installing you will be asked to create a username("postgres") and password("postgres").
  5. Open "pgadmin", authenticate and create database "pokemon_backup".
  6. If you have given username, password and database name other than mentioned in step 4 and 5 then please update the same in settings.py. 
  7. Open command prompt and cd to the project directory in step 1(pokemon-backup-api).
  8. Run "python manage.py runserver".
