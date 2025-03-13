#!/bin/sh
set -e



# rund project
#export FLASK_APP=./app.py
# flask --debug run -h 0.0.0.0


# Start the primary process and put it in the background

flask db upgrade  


echo " RUN SEED"
flask seed run