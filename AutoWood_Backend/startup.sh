#!/bin/sh
python manage.py migrate
python manage.py loaddata initial_json.json
sqlite3 db.sqlite3 'PRAGMA journal_mode=WAL;'
sqlite3 db.sqlite3 'PRAGMA synchronous=1;'
gunicorn --bind :8000 --workers 2 AutoWood_Backend.wsgi:application