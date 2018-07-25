from .base import *

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ttd',
        'USER': os.getenv('DB_USERNAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
