"""Django settings for tests."""

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production

SECRET_KEY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

INTERNAL_IPS = ["127.0.0.1"]

LOGGING_CONFIG = None  # avoids spurious output in tests


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "social_twitter",
    "tests",
]

MEDIA_URL = "/media/"  # Avoids https://code.djangoproject.com/ticket/21451

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tests.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    },
]

STATIC_ROOT = os.path.join(BASE_DIR, "tests", "static")

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "tests", "additional_static"),
    ("prefix", os.path.join(BASE_DIR, "tests", "additional_static")),
]

# Cache and database

CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
    "second": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
}

# if os.environ.get("DJANGO_DATABASE_ENGINE") == "postgresql":
#     DATABASES = {
#         "default": {"ENGINE": "django.db.backends.postgresql", "NAME": "debug-toolbar"}
#     }
# elif os.environ.get("DJANGO_DATABASE_ENGINE") == "mysql":
#     DATABASES = {
#         "default": {"ENGINE": "django.db.backends.mysql", "NAME": "debug_toolbar"}
#     }
# else:
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

# TODO: social twitter config
