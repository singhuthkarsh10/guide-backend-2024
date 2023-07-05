"""
Django settings for guide_project project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import cloudinary.api
import cloudinary.uploader
import cloudinary
import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-bn!gb+_&96p0e7j+0@in%!o5xxl23m$907%3sgyqlekw&85sgv'
SECRET_KEY = os.environ.get('SECRET_KEY')
# DEBUG = os.environ.get('DEBUG')
DEBUG = True

# DATABASE_URL = "postgresql://postgres:4M84u0U9dcm9LmdaH2Ar@containers-us-west-105.railway.app:5862/railway"


ALLOWED_HOSTS = [
    'https://guide-env.eba-uic37c6i.ap-south-1.elasticbeanstalk.com',
    'guide-env.eba-uic37c6i.ap-south-1.elasticbeanstalk.com',
    'https://guideselection.herokuapp.com/',
    'localhost',
    '127.0.0.1',
    'https://www.cse-projectregistration.co.in/',
    'https://cse-projectregistration.co.in/',
    '63.250.59.207',
    '0.0.0.0:8000',
    'cse-projectregistration.co.in',
    'https://guide-backend-production-d238.up.railway.app',
    'guide-backend-production-d238.up.railway.app',
    'https://guide-backend-production.up.railway.app',
    'guide-backend-production.up.railway.app',
    '*',
]

CSRF_TRUSTED_ORIGINS = [
    'https://guide-env.eba-uic37c6i.ap-south-1.elasticbeanstalk.com',
    'https://www.cse-projectregistration.co.in',
    'http://127.0.0.1:8000/',
    'http://127.0.0.1:8000/pride-cell',
    'https://guideselection.herokuapp.com/',
    'https://guide-backend-production.up.railway.app',
    'https://cse-projectregistration.co.in',
    'https://guide-backend-production-d238.up.railway.app'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # custom apps
    'pages',
    'dashboard',
    'comments',
    'accounts',
    # 3rd party apps
    'cloudinary',
    'cloudinary_storage',
    'import_export',
    'storages',
    'whitenoise.runserver_nostatic',
    'verify_email',  # sending email verification
    # 'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 3rd party
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'guide_project.urls'

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

WSGI_APPLICATION = 'guide_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'GUIDE-SELECTION',
        'USER': 'techboizs',
        'PASSWORD': 'AAd!tyAA$ravi',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'GUIDE-TEST',
        'USER': 'techboizs',
        'PASSWORD': 'AAd!tyAA$ravi',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}'''


# Production DB to be used for railway personal

DATABASE_URL = "postgresql://postgres:M5IdDWcXIAhyt06Sh0w0@containers-us-west-132.railway.app:6989/railway"

'''DATABASES = {
    "default": dj_database_url.config(default=os.environ.get('DATABASE_URL'), conn_max_age=None),
}'''
# DATABASES = {
#     "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=None),
# }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# Tells where after performing collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'guide_project/static')
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cloudinary config


cloudinary.config(
    cloud_name="dzg5jildq",
    api_key="321237999372576",
    api_secret="5Gxrc6a6yZxY8QvQlsDPF-9TKnE",
    # upload_prefix="http://api.cloudinary.com",
)


# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Email Configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_USER = 'guideproject2023@gmail.com'
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_PASSWORD = 'rceddrndzxncxiuw'
EMAIL_USE_TLS = True

LOGIN_URL = 'login'

# Email Verify Config

HTML_MESSAGE_TEMPLATE = "verify/acc_active_email.html"
VERIFICATION_SUCCESS_TEMPLATE = "verify/success.html"
VERIFICATION_FAILED_TEMPLATE = "verify/failed.html"
REQUEST_NEW_EMAIL_TEMPLATE = "verify/req_new_email.html"
LINK_EXPIRED_TEMPLATE = 'verify/link_expired.html'
NEW_EMAIL_SENT_TEMPLATE = 'verify/acc_act_email_sent.html'
MAX_RETRIES = 10
EXPIRE_AFTER = "1h"
SUBJECT = 'ACCOUNT VERIFICATION FOR PROJECT REGISTRATION'


# AWS S3 configs
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'django-guide-project-new'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_STORAGE_BUCKET_NAME = 's3-django-test-bucket'
# Logout On Closing
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
