from backend.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'notes',
        'USER': 'eugene',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '5432'
    }
}
