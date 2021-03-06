"""
Django settings for Trainingproject project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(e(gjib$l!g%eu5575a(9+l57n*-z$hm#@iyzms(zf(^+$a&y#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Trainingapp',
    'django.contrib.admin',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'Trainingproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Trainingapp/templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'Trainingproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

from django.core.urlresolvers import reverse_lazy

# It defaults to /accounts/profile/ if it doesn't exist.

LOGIN_REDIRECT_URL = reverse_lazy('dashboard')  # tells django to redirect to this page after login. if there is no next parameter.
# to redirect to login
LOGIN_URL = reverse_lazy('login')  # reverse_lazy is same as reverse, builds the url dynamically by their name.
# to redirect to logout
LOGOUT_URL = reverse_lazy('logout')


# indicates the class to use to send emails,
# EmailBackend allows to write emails to console.
# (yo can see email on ur console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'yourpassword'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# python-social-auth settings
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',

    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
)
SOCIAL_AUTH_GOOGLE_OAUTH2_USE_DEPRECATED_API = True
SOCIAL_AUTH_GOOGLE_PLUS_USE_DEPRECATED_API = True

SOCIAL_AUTH_FACEBOOK_KEY = '233313390510522'
SOCIAL_AUTH_FACEBOOK_SECRET = '35cbe6afa6f0100e19d83519e39c97b2'

SOCIAL_AUTH_TWITTER_KEY = 'kK66CnsawdeyflwbAEus98YxI'
SOCIAL_AUTH_TWITTER_SECRET = 'p0UrT8LsO7lCT1hajsn8ge2PCoC7B0XeLUyUk57ZLWqqdG2arV'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '313681665843-c9nh17kljdo5qtpnt8lv13u6qvmmf883.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'MHkJTbuqnJDE_ihCqIBMXVqM'