from dccwebproject.settings.common import *


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dccwebproject.settings.test")

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'app_db_test'
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

LOGGING = {}
