from dccwebproject.settings.common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0@^9uca^^u3v2^b8^()^&n4eq=)dc!u7m@no-m*wkjv3+k*=8y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dccwebproject.settings.production")

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodatabase',
        'USERNAME' : 'root',
        'PASSWORD' : '',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}