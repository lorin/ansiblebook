#!/usr/bin/env python
# A script to set the site domain
# Assumes two environment variables
#
# WEBSITE_DOMAIN: the domain of the site (e.g., www.example.com)
# PROJECT_DIR: root directory of the project
# PROJECT_APP: name of the project app
import os
import sys

# Add the project directory to system path
proj_dir = os.path.expanduser(os.environ['PROJECT_DIR'])
sys.path.append(proj_dir)

proj_app = os.environ['PROJECT_APP']
os.environ['DJANGO_SETTINGS_MODULE'] = proj_app + '.settings'
import django
django.setup()
from django.conf import settings
from django.contrib.sites.models import Site
domain = os.environ['WEBSITE_DOMAIN']
Site.objects.filter(id=settings.SITE_ID).update(domain=domain)
Site.objects.get_or_create(domain=domain)
