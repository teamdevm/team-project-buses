#!/bin/sh

python init_db.py

gunicorn \
	-w 4 \
	--bind 0.0.0.0:5000 \
	--timeout 600 \
	--access-logfile - \
	buses:app
