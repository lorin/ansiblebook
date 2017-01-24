#!/bin/bash
# Adapted from https://github.com/ansible/django-gulp-nginx
# https://github.com/ansible/django-gulp-nginx/blob/master/ansible/roles/django-gunicorn/files/entrypoint.sh
MANAGE=/srv/project/manage.py
BINDIR=/srv/bin

set -x

if [[ $@ == *"gunicorn"* || $@ == *"runserver"* ]]; then
	if [[ -f $MANAGE ]]; then
        $BINDIR/wait_on_postgres.py
        if [[ $? == 0 ]]; then
            $MANAGE migrate --noinput
            $MANAGE collectstatic --noinput
            $BINDIR/setsite.py
            $BINDIR/setadmin.py
        fi
	fi
fi


