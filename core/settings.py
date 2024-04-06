"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from os import getenv, path
from django.core.management.utils import get_random_secret_key # for generating secret key
import dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

"""
Custom Settings
Check if the environment variables (.env) file exists and load it
"""
dotenv_file = BASE_DIR / '.env'
if path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'weathers',
    'corsheaders',
    'djoser',
    'drf_yasg',
    'users',
    'observations.apps.ObservationsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Allowing frontend to make requests to backend without running into CORS-related issues
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

"""
Custom Settings for API Schema and JWT Authentication 
"""
REST_FRAMEWORK = {
    # 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_SCHEMA_CLASS': 'users.schema_generator.CustomAutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'users.authentication.CustomJWTAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

}

"""
Custom Setting for Authentication Backend
"""
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}

"""
Custom Setting for JWT Authentication by djoser
"""
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'TOKEN_MODEL': None,
    # 'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': allowed_redirect_uris

}
"""
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
"""
EMAIL_HOST = 'mail.rashkemsoft.com.ng'
EMAIL_HOST_USER = 'admin@rashkemsoft.com.ng'
EMAIL_HOST_PASSWORD = 'admin4rashkem'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'admin@rashkemsoft.com.ng'
#abiodunyekeen76@gmail.com
AUTH_COOKIE = 'access'
AUTH_COOKIE_ACCESS_MAX_AGE = 60 * 60 * 5
AUTH_COOKIE_REFRESH_MAX_AGE = 60 * 60 * 24
AUTH_COOKIE_SECURE = getenv('AUTH_COOKIE_SECURE', 'True') == 'True'
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = '/'
AUTH_COOKIE_SAMESITE = 'None'

CORS_ALLOWED_ORIGINS =[]

SITE_NAME = 'Team 2'

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

AUTH_USER_MODEL = 'users.UserAccount'


