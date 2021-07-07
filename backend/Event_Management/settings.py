"""
Django settings for Event_Management project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fl#&&aaz-f_g#d^ce=4jn43v$vo0hqh+lx92@#*11(og*_l$6#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.64', 'localhost', '127.0.0.1', '192.168.1.70', '192.168.1.16']


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'notifications',

	#Foreign apps
	'djoser',
	'corsheaders',
	'rest_framework',
	'rest_framework.authtoken',
	'webpack_loader',

	#Our apps
	'django_registration',
	'resources',
	'main',
	'users',
	'forms',
	'pre_events',
	'events',
	'notificacoes',
]

DJANGO_NOTIFICATIONS_CONFIG = { 'USE_JSONFIELD': True}


NOTIFICATIONS_NOTIFICATION_MODEL = 'notificacoes.Notificacao'


def get_config():
    user_config = getattr(settings, 'DJANGO_NOTIFICATIONS_CONFIG', {})

    config = CONFIG_DEFAULTS.copy()
    config.update(user_config)

    return config


MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'Event_Management.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			Path.joinpath(BASE_DIR, 'templates'),
			Path.joinpath(BASE_DIR, 'resources/templates'),
			Path.joinpath(BASE_DIR, 'users/templates'),
			Path.joinpath(BASE_DIR, 'pre_events/templates')
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

WSGI_APPLICATION = 'Event_Management.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'les',
        'USER': 'admin',
        'PASSWORD' : 'kanguruu',
        'HOST' : 'database-1.cw0weh0ezgyc.eu-west-2.rds.amazonaws.com',
        'PORT' : '3306',
        'OPTIONS' : { 
            "init_command" : "SET sql_mode = 'STRICT_TRANS_TABLES'"
        }
    }
}

MESSAGE_TAGS = {
	messages.DEBUG:    'info',
	messages.INFO:      'info',
	messages.SUCCESS:   'success',
	messages.WARNING:   'warning',
	messages.ERROR:     'danger',
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

DIST_URL = '/static/'
DIST_ROOT = os.path.join(BASE_DIR, '..', 'frontend/', 'dist/')

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "assets/"),
	DIST_ROOT
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

FRONTEND_DIR = os.path.join(BASE_DIR, '../', 'frontend')

WEBPACK_LOADER = {
	'DEFAULT': {
		'CACHE': not DEBUG,
		'BUNDLE_DIR_NAME': 'DIST_URL',
		'STATS_FILE': os.path.join(FRONTEND_DIR, 'webpack-stats.json'),
		'POLL_INTERVAL': 0.1,
		'TIMEOUT': None,
		'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
		'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
	}
}

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': [
		'rest_framework.authentication.TokenAuthentication',
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.SessionAuthentication',
	]
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'dashboard'