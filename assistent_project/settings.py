"""
Django settings for assistent_project project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

AUTH_USER_MODEL = "authentication.User"

SECRET_KEY = os.getenv("SECRET_KEY", "NO_SECRET")

DEBUG = True

ALLOWED_HOSTS = ['*']

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

MEDIA_ROOT = os.path.join(BASE_DIR, r'media')
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'assistent_app',
    'rest_framework',
    'corsheaders',
    "treebeard",
    "core",
    'authentication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'assistent_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'assistent_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASE_ENV = {
    #когда-нибудь вынесем в ENV переменные или файл, как тут https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', "django.db.backends.postgresql"),
        'NAME': "favdeep_database",
        'USER': "favdeep_database_user",
        'PASSWORD': "WozGFnbtNYYiubUfbcuBLhuoNZYr7YVl",
        'HOST': "dpg-cpir66kf7o1s73blgq70-a.frankfurt-postgres.render.com",
        'PORT': 5432,
        'OPTIONS': {
            'sslmode': 'require',  # устанавливаем режим SSL
        }
    }
}

if DATABASE_ENV['default']['ENGINE'] == 'django.db.backends.mysql':
    DATABASE_ENV['default']['OPTIONS'] = {
        'sql_mode': 'ALLOW_INVALID_DATES',
        'charset': 'utf8mb4',
    }

DATABASES = DATABASE_ENV

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[{levelname}]-[{asctime}]-{module} {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
