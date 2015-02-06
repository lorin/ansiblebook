#!/bin/bash
virtualenv venv
source venv/bin/activate
pip install mezzanine
mezzanine-project myproject
cd myproject
python manage.py createdb
python manage.py runserver
