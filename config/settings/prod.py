"""Production settings."""

import os

from .base import *  # noqa: F403

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
    if host.strip()
]


# Database
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'watchstore'),
        'USER': os.environ.get('POSTGRES_USER', 'watchstore'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}


# Email
# https://docs.djangoproject.com/en/6.1/topics/email/#topic-email-configuration

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
        'HOST': os.environ.get('EMAIL_HOST', 'localhost'),
        'PORT': int(os.environ.get('EMAIL_PORT', '587')),
        'HOST_USER': os.environ.get('EMAIL_HOST_USER', ''),
        'HOST_PASSWORD': os.environ.get('EMAIL_HOST_PASSWORD', ''),
        'USE_TLS': os.environ.get('EMAIL_USE_TLS', 'true').lower() == 'true',
    },
}

CACHE = {
    'BACKEND': 'django_redis.cache.RedisCache',
    'LOCATION': os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/1'),
    'OPTIONS': {
        'CLIENT_CLASS': 'django_redis.client.DefualtClient'
    }
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
