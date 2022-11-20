import os
import logging
from pathlib import Path
DEBUG=True
BASE_DIR = Path(__file__).resolve().parent.parent

# telegram msg
TOKEN = SECRET_KEY = os.environ.get('TOKEN_ADMIN_GROUP')
CHANEL = os.environ.get('CHANEL')

SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['djangoin', 'django', os.environ.get('DOMAIN'), f"{os.getenv('COMPOSE_PROJECT_NAME')}_django"]
CSRF_TRUSTED_ORIGINS = [f"https://{os.getenv('DOMAIN')}:{os.getenv('PORT_SSL')}",]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('PG_HOST'),
        'PORT': '',
        'CONN_MAX_AGE': 600
    }
}

STATIC_URL = 'static/'
STATIC_ROOT = '/var/www/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/media'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phone_field',
    'rest_framework',
    'menu.apps.MyConfig',
    'order.apps.OrderConfig'

]
MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    # 'middleware.cache.FetchFromCacheResetCacheMiddleware',

]

ROOT_URLCONF = 'delivery.urls'

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

WSGI_APPLICATION = 'delivery.wsgi.application'


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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Irkutsk'

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]

}


LOGLEVEL = os.getenv('DJANGO_LOGLEVEL', 'debug').upper()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[DJANGO] %(levelname)s %(asctime)s %(module)s '
                      '%(name)s.%(funcName)s:%(lineno)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': LOGLEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': LOGLEVEL,
            'propagate': False,
        }
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_CACHE"),
        # "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# # Key in `CACHES` dict
# CACHE_MIDDLEWARE_ALIAS = 'default'

# # Additional prefix for cache keys
# CACHE_MIDDLEWARE_KEY_PREFIX = ''

# # Cache key TTL in seconds
# CACHE_MIDDLEWARE_SECONDS = 1
# # CACHE_MIDDLEWARE_SECONDS = 3600*24*7
