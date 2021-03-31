import dj_database_url
from decouple import config
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = PROJECT_DIR.parent


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',

    'zackplauche.apps.blog',
    'zackplauche.apps.base.apps.BaseConfig',
    'zackplauche.apps.portfolio',
    'zackplauche.apps.services',

    'storages',
    'tinymce',
    'django_extensions',
    'adminsortable2',
    
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'zackplauche.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_DIR / 'templates',
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

WSGI_APPLICATION = 'zackplauche.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

load_dotenv(find_dotenv())

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=False)
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Custom Authentication
# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/

AUTH_USER_MODEL = 'base.User'


# Amazon S3 Settings (via django-storages & boto3)
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
# Userful article: https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = config('S3_BUCKET_NAME')

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400', 
    'ACL': 'public-read'
}

AWS_QUERYSTRING_AUTH = False

AWS_DOMAIN_NAME = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

AWS_LOCATION = 'static'


# Static files (CSS, JavaScript, Images)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_DIRS = [
    PROJECT_DIR / 'static',
]


# Email Settings
# https://docs.djangoproject.com/en/3.1/topics/email/

EMAIL_PORT = 587

EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

CUSTOMER_SUPPORT_EMAILS = [DEFAULT_FROM_EMAIL,]


# TinyMCE Rich Text Editor
# https://django-tinymce.readthedocs.io/en/latest/

TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 300,
    "menubar": False,
    "plugins": 'lists',
    "toolbar": 'undo redo | formatselect | '
    'bold italic backcolor | alignleft aligncenter '
    'alignright alignjustify | bullist numlist outdent indent | '
    'removeformat | help',
}

