#!/bin/bash
# Adapted from https://github.com/ansible/django-gulp-nginx
MANAGE=/srv/project/manage.py

set -x

if [[ $@ == *"gunicorn"* || $@ == *"runserver"* ]]; then
	if [[ -f $MANAGE ]]; then
	$MANAGE migrate --noinput
	$MANAGE collectstatic --noinput
	/srv/bin/setsite.py
	/srv/bin/setadmin.py
	fi
fi


