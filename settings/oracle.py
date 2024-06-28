"""
Django settings for pyfic project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django_extensions',
    'faker_meta_db'
]

DATABASES = {
    'SCHEMA1': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'FREE',
        'USER': 'C##SCHEMA1',
        'PASSWORD': 'pass4C##SCHEMA',
        'HOST': 'oracledb',
        'PORT': '1521',
    },
    'SCHEMA2': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'FREE',
        'USER': 'C##SCHEMA2',
        'PASSWORD': 'pass4C##SCHEMA',
        'HOST': 'oracledb',
        'PORT': '1521',
    },
    'SCHEMA3': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'FREE',
        'USER': 'C##SCHEMA3',
        'PASSWORD': 'pass4C##SCHEMA',
        'HOST': 'oracledb',
        'PORT': '1521',
    }, 
    'SCHEMA4': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'FREE',
        'USER': 'C##SCHEMA4',
        'PASSWORD': 'pass4C##SCHEMA',
        'HOST': 'oracledb',
        'PORT': '1521',
    },
    'SCHEMA5': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'FREE',
        'USER': 'C##SCHEMA5',
        'PASSWORD': 'pass4C##SCHEMA',
        'HOST': 'oracledb',
        'PORT': '1521',
    }, 
    'SCHEMA6': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'FREE',
        'USER': 'C##SCHEMA6',
        'PASSWORD': 'pass4C##SCHEMA',
        'HOST': 'oracledb',
        'PORT': '1521',
    }, 
    'SCHEMA7': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'FREE',
        'USER': 'C##SCHEMA7',
        'PASSWORD': 'pass4C##SCHEMA',
        'HOST': 'oracledb',
        'PORT': '1521',
    },
    'SCHEMA8': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'FREE',
        'USER': 'C##SCHEMA8',
        'PASSWORD': 'pass4C##SCHEMA',
        'HOST': 'oracledb',
        'PORT': '1521',
    },
    'SCHEMA9': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'FREE',
        'USER': 'C##SCHEMA9',
        'PASSWORD': 'pass4C##SCHEMA',
        'HOST': 'oracledb',
        'PORT': '1521',
    },
    'SCHEMA10': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'FREE',
        'USER': 'homelab',
        'PASSWORD': 'home1234',
        'HOST': 'oracledb',
        'PORT': '1521',
    },
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'FREE',
        'USER': 'homelab',
        'PASSWORD': 'home1234',
        'HOST': 'oracledb',
        'PORT': '1521',
    }
}



