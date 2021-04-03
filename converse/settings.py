"""
Django settings for converse project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
# for the database thing (second one)
import pymongo

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1)9otfvin3)ud)(pr+$8h(nsaw_zym^_s@bvv_o$okzrdzv65u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# contains address of hosted websites
ALLOWED_HOSTS = []

# during development work only
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    
# for the accounts apps
# user management database
AUTH_USER_MODEL = 'account.Account'
AUTHENTICATION_BACKENDS = ( 
    'django.contrib.auth.backends.AllowAllUsersModelBackend', 
    'account.backends.CaseInsensitiveModelBackend',
)

# Application definition

INSTALLED_APPS = [
    # add the name of your app 
    'chatapp',
    'room', # this one for chatroom (no database)
    'account',  # this one for user management
    'friends', # for the friend system app
    # we didn't used this
    # 'chatroom', # this is for the public chatrooms
    'quickchat', # this is for the limited chatroom
    'privatechat', # for chatting with friends
     # for Blogs and Forums
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',  # channels support
    'django.contrib.humanize',  # timestamp support

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'converse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # add link to the template directories
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Web Server Gateway Interface
WSGI_APPLICATION = 'converse.wsgi.application'

# ASGI (Asynchronous Server Gateway Interface) 
# added this for channels
# ASGI_APPLICATION = "converse.routing.application"

# for routing of web sockets (using asgi)
ASGI_APPLICATION = "converse.asgi.application"  


# for channels reddis (runs on port 6379)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# postgresql
# DB_NAME = "converse"
# DB_USER = "dsm"
# DB_PASSWORD = "Dharam@098"
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': DB_NAME,
#         'USER': DB_USER,
#         'PASSWORD': DB_PASSWORD,
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
#postgresql
DB_NAME = 'converse'
DB_USER = 'prasun'
DB_PASSWORD = "zxcvbnm"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# to access the static, media files
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')

TEMP = os.path.join(BASE_DIR, 'media_cdn/temp')

BASE_URL = "http://127.0.0.1:8000"

# for uploading image or text
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760 # 10mb = 10 * 1024 *1024


# database mongo thing (for second one)
MONGO_CLIENT = pymongo.MongoClient()

# session settings
SESSION_COOKIE_AGE = 5 * 60 # maybe session limit
SESSION_SAVE_EVERY_REQUEST = True