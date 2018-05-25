from .common import *
from decouple import config,Csv
from django.conf.urls.static import static
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG = TEMPLATE_DEBUG = True

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
