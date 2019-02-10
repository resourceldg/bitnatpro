import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = ('peluca', 'resourceldg@gmail.com')
MANAGERS = ('pelucas', 'resourceldg@gmail.com')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'bitnativo@gmail.com'
EMAIL_HOST_PASSWORD = 'bitnativogmail'
EMAIL_PORT = 465


SECRET_KEY = '*fkewr^5v&!sz4(+0=v)c%h1)6tw_+m_-2zo)+^srum871j*_s'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bitnat',
    'django_comments',
    'mptt',
    'zinnia',
    'tagging',

]

ROOT_URLCONF = 'btn.urls'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'base',
        'USER': 'btn',
        'PASSWORD': 'btn',
        'HOST': 'localhost',
        'PORT': '',
    }
}


STATIC_URL = '/static/'

STATICFILES_DIRS = os.path.join(BASE_DIR, "static_pro", "static"),
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_s", "static_root") 
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_s", "media_root")

