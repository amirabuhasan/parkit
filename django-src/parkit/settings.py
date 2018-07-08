"""
Django settings for parkit project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm)5*skk7ft-byfe*t+xi0i!w12qua%!fn7+@s62l9r#o_z28)='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://parkit-testsite.firebaseapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_filters',
    'accounts',
    'vehicle',
    'search',
    'rent',
    'profile',
    'rest_auth',
    'rest_framework',
    'rest_framework_jwt',
    'corsheaders',
    'drf_multiple_model',
    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = DEBUG
CORS_REPLACE_HTTPS_REFERER = DEBUG
ROOT_URLCONF = 'parkit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'parkit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'parkit',                      
#        'USER': 'parkitadmin',
#        'PASSWORD': 'qwerty123',
#        'HOST': 'parkit-backend.cmwyopnebff9.ap-southeast-1.rds.amazonaws.com',
#        'PORT': '5432',
#    }
#}

if DEBUG is False:
    if 'RDS_HOSTNAME' in os.environ:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.environ['RDS_DB_NAME'],
                'USER': os.environ['RDS_USERNAME'],
                'PASSWORD': os.environ['RDS_PASSWORD'],
                'HOST': os.environ['RDS_HOSTNAME'],
                'PORT': os.environ['RDS_PORT'],
            }
        }

if DEBUG is True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'parkitdb',                      
            'USER': 'parkitadmin',
            'PASSWORD': 'qwerty123',
            'HOST': 'parkit-db.cmwyopnebff9.ap-southeast-1.rds.amazonaws.com',
            'PORT': '5432',
        }
    }

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'parkit-backend',                      
#        'USER': 'parkitadmin',
#        'PASSWORD': 'qwerty123',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIR = [
    os.path.join(os.path.dirname(BASE_DIR),"static_cdn")
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_cdn")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"media")

MEDIA_URL = "/media/"

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    "DEFAULT_PERMISSION_CLASSES": (
        'rest_framework.permissions.IsAuthenticated',
    ),

    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ), 

    "DEFAULT_FILTER_BACKENDS": (
        'django_filters.rest_framework.DjangoFilterBackend',
    )
}

REST_USE_JWT = True

JWT_AUTH = {
 
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=259200),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_PAYLOAD_HANDLER': 'accounts.api.custom_jwt.custom_jwt_payload_handler',    
 
}

#For email
EMAIL_USE_TLS      = True
DEFAULT_FROM_EMAIL = 'noreply.support@parkitmy.com'
EMAIL_BACKEND      = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST         = 'smtp.gmail.com'
EMAIL_HOST_USER    = 'noreply.support@parkitmy.com'
EMAIL_HOST_PASSWORD = 'Iamsupportnoreply'
EMAIL_PORT = 587


SITE_ID = 2

REST_SESSION_LOGIN = True
AUTH_USER_MODEL = 'accounts.User'

REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER': 'accounts.api.serializers.PasswordResetSerializer',
}