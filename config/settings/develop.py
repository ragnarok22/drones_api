"""
This is the settings file that you use when you're working on the project locally.
Local development-specific include DEBUG mode, log level, and activation of developer tools like django-debug-toolsbar
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qov#ce&bl3z8@ymehv1byt^beru%el-0wjo%e#1q8#og6331ik'

ALLOWED_HOSTS = ['*']

MEDIA_ROOT = os.path.join(BASE_DIR, 'drones_api', 'media')

# email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
