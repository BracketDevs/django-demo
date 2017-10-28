"""
Django settings for django_demo project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# If your secret key's available, your whole app is compromised. If that app is deployed on a server,
# then your server's security is potentially compromised: as the secret key can be used to sign malicious code, etc
# Take your key out of version control, and use environment variables - http://heldercorreia.com/blog/secrets-in-the-environment
SECRET_KEY = 'oesxk=)*h!tdkoer60i98d^&)d56u%h*-sx_2(m!p*e0vf^k)k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG:
    # Deprecated. https://docs.djangoproject.com/en/1.9/ref/settings/#template-debug
    TEMPLATE_DEBUG= True
    # see all of Djangos debug logging which is very verbose as it includes all database queries. Info default
    os.environ['DJANGO_LOG_LEVEL'] = 'DEBUG'


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # default applications are included for the common case, but not everybody needs them
    'django.contrib.admin', # admin site
    'django.contrib.auth', # authentication system
    'django.contrib.contenttypes', # framework for content types
    'django.contrib.sessions', # session framework
    'django.contrib.messages', # messaging framework
    'django.contrib.staticfiles', # framework for managing static files.
    'rango',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Django provides a template context processor https://docs.djangoproject.com/en/1.9/ref/templates/api/#django-template-context-processors-media
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'django_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/' # location with which clients can access static content
STATICFILES_DIRS = [STATIC_DIR, ] # server-side locations

# Media files
# The vars will be picked up and used by Django to set up media file hosting https://docs.djangoproject.com/en/1.9/howto/static-files/#serving-files-uploaded-by-a-user-during-development
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

# Setup Logging
# https://docs.djangoproject.com/en/1.9/topics/logging/

if DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'rango': {
                'handlers': ['console'],
                'propagate': False,
                'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            },
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        }
    }