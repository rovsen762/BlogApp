from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'https://*.mydomain.com',
    'https://*.127.0.0.1',
    'http://localhost:5001',
    'http://159.65.125.201:5001',

]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'microservice'),
        'USER': os.getenv('POSTGRES_USER', 'blog'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'blog'),
        'HOST': os.getenv("DB_HOST", "postgresdb"),
        'PORT': os.getenv("DB_PORT", "5432"),
    }
}

#adlarini nece deyisim bilmedim