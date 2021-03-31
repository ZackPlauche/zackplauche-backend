from zackplauche.settings.prod import ALLOWED_HOSTS
from .base import *

SECRET_KEY = 'dummy_key'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Staticfiles Settings

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_ROOT = PROJECT_DIR / 'media'

MEDIA_URL = '/media/'



# Email Settings

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = config('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')