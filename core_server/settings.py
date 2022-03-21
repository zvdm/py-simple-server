import os
from pathlib import Path

from environs import Env

env = Env()
env.read_env()

# ==================================== DATABASE =================================== #
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST", "localhost"),
        "PORT": env.int("POSTGRES_PORT", 5432),
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
# ================================ END DATABASE =================================== #

# ================================== DJANGO CORE ================================== #
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = []

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

DEBUG = env.bool("DEBUG")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
]

LANGUAGE_CODE = "en-us"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core_server.urls"

SECRET_KEY = env("SECRET_KEY")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.csrf",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

TIME_ZONE = env("TIME_ZONE", "UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = False

WSGI_APPLICATION = "core_server.wsgi.application"
# ================================ END DJANGO CORE ================================ #

# =============================== MEDIA AND STATIC ================================ #
STATIC_URL = "/static/"
STATIC_ROOT = "/var/www/static"  # to collect static files in docker containers and share with Nginx
# ============================= END MEDIA AND STATIC ============================== #

# =================================== MAILING ===================================== #
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    EMAIL_HOST_USER = "info@example.com"
else:
    DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
    SERVER_EMAIL = env("SERVER_EMAIL")

    with env.prefixed("EMAIL_"):
        EMAIL_HOST = env("HOST")
        EMAIL_HOST_PASSWORD = env("HOST_PASSWORD")
        EMAIL_HOST_USER = env("HOST_USER")
        EMAIL_PORT = env.int("PORT")
        EMAIL_TIMEOUT = env.int("TIMEOUT", 20)
        EMAIL_USE_TLS = env.bool("USE_TLS")
# ================================= END MAILING =================================== #

# ===================================== MAPS ====================================== #
MAPS_API_KEY = env("MAPS_API_KEY")
# =================================== END MAPS ==================================== #
