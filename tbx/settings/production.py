from .base import *
from urllib.parse import urlparse
import os


env = os.environ.copy()
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
        'INDEX': 'wagtail-torchbox'
    }
}


INSTALLED_APPS += (
    'wagtail.contrib.wagtailfrontendcache',
)

redis_url = urlparse(os.environ.get('REDISCLOUD_URL'))
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
        'KEY_PREFIX': 'torchbox',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

SERVER_EMAIL = "root@by-web-2.torchbox.com"

# AWS_QUERYSTRING_AUTH = False
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# MEDIA_URL = 'http://%s.s3-website-ap-northeast-1.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"

# Facebook JSSDK app Id
FB_APP_ID = '1687713411443460'

try:
    from .local import *
except ImportError:
    pass
