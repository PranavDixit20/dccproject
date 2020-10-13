from .common import *
from decouple import config,Csv
from django.conf.urls.static import static
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG = TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
