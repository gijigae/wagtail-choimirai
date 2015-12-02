from .base import *

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


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
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

COMPRESS_ENABLED = True

SERVER_EMAIL = "root@by-web-2.torchbox.com"


# Facebook JSSDK app Id
FB_APP_ID = '1687713411443460'


try:
    from .local import *
except ImportError:
    pass
