from __future__ import unicode_literals
import multiprocessing
import os

bind = "0.0.0.0:{}".format(os.environ.get("GUNICORN_PORT", 8000))
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = "error"
proc_name = "mezzanine"
