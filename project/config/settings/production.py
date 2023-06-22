from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://*.mydomain.com','https://*.127.0.0.1','http://localhost']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'blog'),
        'USER': os.getenv('POSTGRES_USER', 'blog'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'blog'),
        'HOST': os.getenv("DB_HOST", "postgresdb"),
        'PORT': os.getenv("DB_PORT", "5432"),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', "")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

