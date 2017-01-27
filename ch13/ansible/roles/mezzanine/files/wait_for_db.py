#!/usr/bin/env python
import os
import psycopg2
import sys
import time

dbname = os.environ.get("DATABASE_NAME", ""),
user = os.environ.get("DATABASE_USER", ""),
password = os.environ.get("DATABASE_PASSWORD", ""),
host = os.environ.get("DATABASE_HOST", "postgres"),
port = int(os.environ.get("DATABASE_PORT", "5432"))

attempts = 0
max_attempts = 20

while True:
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        # If we reach here, we're done
        print("Connected to database {}".format(host))
        sys.exit(0)
    except Exception as e:
        attempts += 1
        if attempts > max_attempts:
            print("Unable to connect to database")
            print(e)
            sys.exit(1)

        time.sleep(3)



