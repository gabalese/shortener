#!/bin/sh
cd /code/shortner
python ./manage.py syncdb --noinput
python ./manage.py migrate --noinput
python ./manage.py runserver 0.0.0.0:8000
