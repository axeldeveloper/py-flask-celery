#!/bin/sh

# turn on bash's job control
#set -m


# rund project
#export FLASK_APP=./app.py
# flask --debug run -h 0.0.0.0


# Start the primary process and put it in the background
gunicorn --bind 0.0.0.0:5000 wsgi:application --log-level=debug
# gunicorn --bind 0.0.0.0:5000 wsgi:app --log-level=debug --workers=2 &

# cron
#cron -f &

#celery
#celery -A myapp.celery worker --loglevel=INFO

# now we bring the primary process back into the foreground
# and leave it there
#fg %1
