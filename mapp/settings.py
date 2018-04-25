import os, dj_database_url, ssl
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['127.0.0.1', 'm-shopping.herokuapp.com', 'mshoppingke.herokuapp.com']


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'products',
    'orders',
    'address',
    'customers',
    'store',
    'storages',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 20
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mapp.urls'

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

WSGI_APPLICATION = 'mapp.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
    os.path.join(BASE_DIR, 'mediafiles'),
)

APPEND_SLASH = True
SITE_ID = 1
DEBUG_COLLECTSTATIC = 1
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = "mapp.s3utils.StaticS3BotoStorage"
DEFAULT_FILE_STORAGE = "mapp.s3utils.MediaS3BotoStorage"


if hasattr(ssl, '_create_unverified_context'):
   ssl._create_default_https_context = ssl._create_unverified_context

db_link = config('DATABASE_URL', os.environ.get("DATABASE_URL", ""))  # os.environ.get("DATABASE_URL", "")
DATABASES = {'default': dj_database_url.config(default=db_link)}

DEBUG = config('DEBUG', os.environ.get("DEBUG", ""), cast=bool)

AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECRET_ACCESS_KEY = config('AWS_S3_SECRET_ACCESS_KEY', os.environ.get("AWS_S3_SECRET_ACCESS_KEY", ""))  # os.environ.get("AWS_S3_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', os.environ.get("AWS_STORAGE_BUCKET_NAME", ""))  # os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_S3_HOST = config('AWS_S3_HOST', os.environ.get("AWS_S3_HOST", ""))  # os.environ.get("AWS_S3_HOST", "")
AWS_S3_ACCESS_KEY_ID = config('AWS_S3_ACCESS_KEY_ID', os.environ.get("AWS_S3_ACCESS_KEY_ID", ""))  # os.environ.get("AWS_S3_ACCESS_KEY_ID", "")