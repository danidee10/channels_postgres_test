import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)
logging.getLogger("channels_postgres.database").setLevel(logging.DEBUG)
# logging.getLogger("psycopg.pool").setLevel(logging.INFO)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-your-secret-key-here"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "channels",
    "channels_postgres",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "core.asgi.application"


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_postgres.core.PostgresChannelLayer",
        "CONFIG": {
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "password",
            "HOST": "127.0.0.1",
            "PORT": "5432",
            "TIME_ZONE": "UTC",
        },
    },
    "redis": {
        "BACKEND": "channels_redis.pubsub.RedisPubSubChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "127.0.0.1",
        "PORT": "5432",
        "CONN_MAX_AGE": 300,
    },
    "channels_postgres": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "127.0.0.1",
        "PORT": "5432",
        "CONN_MAX_AGE": 300,
    },
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ASGI_APPLICATION = "core.asgi.application"
