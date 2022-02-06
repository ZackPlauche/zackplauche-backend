from decouple import config
import django_on_heroku

from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'api.zackplauche.com',
    'zackplauche.com',
    'www.zackplauche.com',
]

CORS_ALLOWED_ORIGINS = [
    'https://www.zackplauche.com/',
    'https://zackplauche.com/',
    'http://zackplauche.com/',
    'http://www.zackplauche.com/',
]

# AWS S3 Storage

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' # TODO Fill this in.

ACL_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

AWS_LOCATION = 'static'

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {'Access-Control-Allow-Origin': '*'}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

django_on_heroku.settings(locals())
del DATABASES['default']['OPTIONS']['sslmode']