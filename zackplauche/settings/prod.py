import django_on_heroku
from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'www.zackplauche.com',
    'zackplauche.com',
    'zackplauche.herokuapp.com',
]


# Staticfiles Settings

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'

STATIC_URL = f'https://{AWS_DOMAIN_NAME}/static/'


# Email Settings

EMAIL_HOST = config('MAILGUN_SMTP_SERVER')

EMAIL_HOST_USER = config('MAILGUN_SMTP_LOGIN')

EMAIL_HOST_PASSWORD = config('MAILGUN_SMTP_PASSWORD')

# Heroku Settings
# https://devcenter.heroku.com/articles/django-app-configuration

django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']