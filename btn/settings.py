# -*- coding: utf-8 -*-
"""
Django settings for btn project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from .info import *
os.environ['wsgi.url_scheme'] = 'https'


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY 

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE  = True
SESSION_COOKIE_SECURE  = True
USE_X_FORWARDED_HOST = True


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.bitnativo.com','168.181.185.152']

ADMINS = ADMINS
MANAGERS = ADMINS

SITE_ID = 2


EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_USE_SSL = EMAIL_USE_SSL
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT


# Application definition

INSTALLED_APPS = INSTALLED_APPS

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware' ,
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware' ,
]

# Key in `CACHES` dict
# CACHE_MIDDLEWARE_ALIAS = 'default'

 # Additional prefix for cache keys
# CACHE_MIDDLEWARE_KEY_PREFIX = ''

 # Cache key TTL in seconds
# CACHE_MIDDLEWARE_SECONDS = 600

ROOT_URLCONF = ROOT_URLCONF

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
               'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'zinnia.context_processors.version',
            ],
        },
    },
]

WSGI_APPLICATION = 'btn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES =  DATABASES

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = STATIC_URL

STATICFILES_DIRS = STATICFILES_DIRS
MEDIA_URL = MEDIA_URL


STATIC_ROOT = STATIC_ROOT
MEDIA_ROOT = MEDIA_ROOT

CACHES = {
   'default' : {
      'BACKEND' : 'django.core.cache.backends.db.DatabaseCache' ,
      'LOCATION' : 'my_cache_table' ,
     }
}
