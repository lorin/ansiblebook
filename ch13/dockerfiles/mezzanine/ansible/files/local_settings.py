from __future__ import unicode_literals
import os

SECRET_KEY = os.environ.get("SECRET_KEY", "")
NEVERCACHE_KEY = os.environ.get("NEVERCACHE_KEY", "")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "")

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": os.environ.get("DATABASE_NAME", ""),
        # Not used with sqlite3.
        "USER": os.environ.get("DATABASE_USER", ""),
        # Not used with sqlite3.
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", ""),
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": os.environ.get("DATABASE_HOST", ""),
        # Set to empty string for default. Not used with sqlite3.
        "PORT": os.environ.get("DATABASE_PORT", "")
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = "mezzanine"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": os.environ.get("MEMCACHED_LOCATION", "memcached:11211"),
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

TWITTER_ACCESS_TOKEN_KEY = os.environ.get("TWITTER_ACCESS_TOKEN_KEY ", "")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET ", "")
TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY ", "")
TWITTER_CONSUMER_SERCRET = os.environ.get("TWITTER_CONSUMER_SERCRET ", "")
TWITTER_DEFAULT_QUERY = "from:ansiblebook"
