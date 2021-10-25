#!/bin/bash

# Collect static files
echo "Collect static files"
python3 manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
# wait for postgres
if [[ $PRODUCTION -eq 1 ]];
  then
    pid_file='data/postmaster.pid'
    while [[ ! -f $pid_file ]]; do sleep 1; echo 'Waiting for postgres to start.'; done;
fi
python3 manage.py makemigrations
python3 manage.py makemigrations config bank attendance
python3 manage.py migrate

# Add initial configs
echo "Running initial configuration"
python3 manage.py createsuperuser --noinput
python3 manage.py shell < $PWD/deploy/docker/app/init_db.py

# Start server
echo "Starting server"
gunicorn --bind :80 yg_system.wsgi:application