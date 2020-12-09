"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APP_BASE_DIR = os.path.join(BASE_DIR, 'app')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@aiopi+=62n6h5&=pdpx8ts=z3ga22+vjuy#98o7b@sbsz-pkb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost' , '127.0.0.1','квест.рф']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'corsheaders',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Для исп-я rest_framework
    'app',  # Папка с файлами сервера
    'djoser',  # Библиотека для авторизации по токену
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True # If this is used then `CORS_ORIGIN_WHITELIST` will not have any effect
CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'tvoyquest',
'USER': 'student',
'HOST': 'localhost',
'PASSWORD': 'iamstudent',

}
}

SIMPLE_JWT = {
'AUTH_HEADER_TYPES': ('JWT',),
}
# Шаблон djoser
DJOSER = {
'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
'ACTIVATION_URL': '#/activate/{uid}/{token}',
'SEND_ACTIVATION_EMAIL': False,
'SERIALIZERS': {
    'user': 'app.serializers.UserSerializer',
    'current_user': 'app.serializers.UserSerializer',
},
}

REST_FRAMEWORK = {
# Используем для доступа django стандарты,
# Доступ только чтение для неавторизированных пользователей.
'DEFAULT_PERMISSION_CLASSES': [
],
'DEFAULT_AUTHENTICATION_CLASSES': (
'rest_framework.authentication.TokenAuthentication', # Указываем тип авторизации
'rest_framework_simplejwt.authentication.JWTAuthentication', #Не забудьте изменить настройки аутентификации для DRF, чтобы отразить использование JWTS.

# (...)
),
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

STATIC_URL = '/static/'
MEDIA_URL = 'media/'
STATIC_ROOT = os.path.join(APP_BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(APP_BASE_DIR,'media')