"""
Django settings for emailwebsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gs=1m4qmq&yjg=7ota!kj3*=s7^v!5zl$+=zs7c+=$(un6-o$n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'djangular',
    'emailclient',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
  'social.backends.google.GoogleOpenId',
  'social.backends.google.GoogleOAuth2',
  'social.backends.google.GoogleOAuth',
  'social.backends.google.GooglePlusAuth',
  'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'emailwebsite.urls'

WSGI_APPLICATION = 'emailwebsite.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Authentication settings

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/emailclient'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'

SOCIAL_AUTH_GOOGLE_PLUS_KEY = '223437181852-e7c5jdibmchc76klsljed1o6r5ne1jp6.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = 'lN2ui_sZgzjfW6JnB1bwFNdt'

SOCIAL_AUTH_GOOGLE_PLUS_SCOPE = ['https://www.googleapis.com/auth/plus.login',
                                 'https://www.googleapis.com/auth/plus.profile.emails.read',
                                 'https://www.googleapis.com/auth/userinfo.email',
                                 'https://www.googleapis.com/auth/userinfo.profile',
                                 'https://mail.google.com/']

GOOGLE_PLUS_AUTH_EXTRA_ARGUMENTS = {'approval_prompt': 'force'} 
#Email settings

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
