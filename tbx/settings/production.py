from .base import *
from urllib.parse import urlparse
import os


env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DEBUG = False

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

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


COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

SERVER_EMAIL = "root@by-web-2.torchbox.com"


# Facebook JSSDK app Id
FB_APP_ID = '1687713411443460'


try:
    from .local import *
except ImportError:
    pass
