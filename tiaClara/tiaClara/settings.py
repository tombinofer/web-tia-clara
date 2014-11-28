# -*- coding: utf-8 -*-
"""
Django settings for tiaClara project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'em=srg%s=80d$h7m8ay-%+j(j_r7_k(6ol7kx-9$n11vi4j(fy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (
    (u'Fernando Orozco', 'fernandogorozco@gmail.com'),
)

MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'productos',
    'contenidos',
    'imagekit',
    'contact_form',
    'ckeditor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tiaClara.urls'

WSGI_APPLICATION = 'tiaClara.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Mendoza'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#Para la llamada de los static y media!
TEMPLATE_DIRS = [os.path.join(BASE_DIR, "templates")]

STATIC_URL = '/static/'
INTERNAL_IPS = ("127.0.0.1",)
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
###################################

#Para la implementación de ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Anchor',
             '-', 'Styles', 'Format',
             '-', 'TextColor', 'BGColor',
             '-', 'SpellChecker', 'Scayt',
             '-', 'Maximize',
             ],
            ['HorizontalRule',
             '-', 'Image', 'Iframe', 'Flash', 'Table', 
             '-', 'BulletedList', 'NumberedList',
             '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
             '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
             '-', 'SpecialChar',
             '-', 'Source',
             ]
        ],
        'language': 'es',
        'scayt_sLang': 'es_ES',
        'wsc_lang': 'es_ES',
        'extraAllowedContent': 'iframe[src,width,height,frameborder,style]',
        'width': '100%',
    },
}


###################################

#configuraciones para enviar mensajes usando gmail
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'webtiaclara@gmail.com'
EMAIL_HOST_PASSWORD = 'webtiaclara1234'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'webtiaclara@gmail.com'
###################################
try:
    from settings_local import *
except ImportError:
    pass