#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn boardgames_home.wsgi:application --bind 0.0.0.0:8000