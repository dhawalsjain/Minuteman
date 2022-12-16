"""
Django settings for boston project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
import boto3
import json

# get database secret and machine cwid secret

region_name = "us-east-1"

AppName = "machinecwid"

client = boto3.client(service_name='secretsmanager', region_name=region_name)
response = client.get_secret_value(SecretId=AppName)
secretDict = json.loads(response['SecretString'])

machinecwid = secretDict['cwid']
machinecwidpassword = secretDict['password']

client = boto3.client(service_name='secretsmanager', region_name=region_name)
response = client.get_secret_value(SecretId=AppName)
secretDict = json.loads(response['SecretString'])

machinecwid = secretDict['cwid']
machinecwidpassword = secretDict['password']

AppName = "MinutemanDB"

client = boto3.client(service_name='secretsmanager', region_name=region_name)
response = client.get_secret_value(SecretId=AppName)
secretDict = json.loads(response['SecretString'])

db_user = secretDict['username']
db_password = secretDict['password']
db_host = secretDict['host']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1$n-&9s7(olmn@aetuhm7gk4ei7l2smujyz8rx)r4h8@)tbo)q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'boston',
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

ROOT_URLCONF = 'boston.urls'

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

WSGI_APPLICATION = 'boston.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'config',
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

import ldap
from django_auth_ldap.config import LDAPSearch,GroupOfNamesType

AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_LDAP_SERVER_URI = "ldap://by0rmr.Company.cnb:3268"
AUTH_LDAP_BIND_DN = "CN=" + machinecwid + ",OU=Users,OU=US,OU=Countries,DC=Company,DC=cnb"
AUTH_LDAP_BIND_PASSWORD = machinecwidpassword

AUTH_LDAP_USER_SEARCH = LDAPSearch("DC=Company,DC=cnb",
                                   ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("OU=Groups,OU=IAM,OU=_DomainOperations,DC=Company,DC=cnb",
    ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr='CN')

AUTH_LDAP_REQUIRE_GROUP = 'CN=ef.u.minuteman_user_management,OU=Groups,OU=IAM,OU=_DomainOperations,DC=Company,DC=cnb'

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    'is_active': 'CN=ef.u.minuteman_user_management,OU=Groups,OU=IAM,OU=_DomainOperations,DC=Company,DC=cnb',
    'is_staff': 'CN=ef.u.minuteman_user_management,OU=Groups,OU=IAM,OU=_DomainOperations,DC=Company,DC=cnb',
}

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

AUTH_LDAP_ALWAYS_UPDATE_USER = False
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_TIMEOUT = 3600

LOGIN_REDIRECT_URL = '/'
X_FRAME_OPTIONS = 'SAMEORIGIN'