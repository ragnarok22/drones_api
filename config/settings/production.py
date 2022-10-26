from .base import *

ALLOWED_HOSTS = ['*']
DEBUG = False

SECRET_KEY = get_env_variable("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_variable('DB_NAME'),
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
