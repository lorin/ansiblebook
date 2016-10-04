#!/bin/bash
virtualenv venv
source venv/bin/activate
pip install mezzanine
mezzanine-project myproject
cd myproject
sed -i.bak 's/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = ["127.0.0.1"]/' myproject/settings.py
python manage.py createdb
python manage.py runserver
