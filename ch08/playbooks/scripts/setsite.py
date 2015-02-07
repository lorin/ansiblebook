#!/usr/bin/env python
# A script to set the site domain
# Assumes two environment variables
#
# PROJECT_DIR: the project directory (e.g., ~/projname)
# WEBSITE_DOMAIN: the domain of the site (e.g., www.example.com)

import os
import sys

# Add the project directory to system path
proj_dir = os.path.expanduser(os.environ['PROJECT_DIR'])
sys.path.append(proj_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.conf import settings
from django.contrib.sites.models import Site

domain = os.environ['WEBSITE_DOMAIN']
Site.objects.filter(id=settings.SITE_ID).update(domain=domain)
Site.objects.get_or_create(domain=domain)

