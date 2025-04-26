import os
from .base import *

DEBUG = False

SECRET_KEY = "nmdrm)x)*@w!mt!6lm+5b7w!fma$y4gs6cjc1d3sp81(58i*vc"
ALLOWED_HOSTS = [
    "localhost",
    "wagtailsite.peoplepower21.org",
    "*",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "siesto",
        "USER": "siesto",
        "PASSWORD": "wagtaildb",
        "HOST": "localhost",
        "PORT": "",
    }
}

cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/cache",
    }
}

import sentry_sdk

sentry_sdk.init(
    dsn="https://d62379f1a632e05a4141ef0084331738@o521974.ingest.us.sentry.io/4509219624714240",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)
try:
    from .local import *
except ImportError:
    pass
