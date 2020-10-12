import os
import django_heroku
import dj_database_url
import dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG'] == 'True'

ALLOWED_HOSTS = [
    'www.zackplauche.com',
    'zackplauche.com',
    'zackplauche.herokuapp.com',
    '127.0.0.1', 
    'localhost'
]


# Application definition

INSTALLED_APPS = [
    'tinymce',
    'blog',
    'base.apps.BaseConfig',
    'portfolio',
    'storages',
    'django_extensions',
    'adminsortable2',
    'services.apps.ServicesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'django.templatetags.static',
            ]
        },
    },
]

WSGI_APPLICATION = 'zackplauche.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=False)


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

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
# AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400', 
    'ACL': 'public-read'
}

AWS_QUERYSTRING_AUTH = False
AWS_DOMAIN_NAME = f'http://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_LOCATION = 'static'

STATIC_URL = AWS_DOMAIN_NAME + '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "/zackplauche/media/")
MEDIA_URL = '/media/'


# Email Settings
# https://docs.djangoproject.com/en/3.1/topics/email/

if DEBUG:
    EMAIL_HOST = 'smtp.gmail.com'
    
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']

    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

else:
    EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']

    EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']

    EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']

EMAIL_PORT = 587

EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']

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

# Heroku Settings
# https://devcenter.heroku.com/articles/django-app-configuration

django_heroku.settings(locals())
del DATABASES['default']['OPTIONS']['sslmode']
