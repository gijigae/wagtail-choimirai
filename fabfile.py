from __future__ import with_statement
from fabric.api import *

import uuid

env.roledefs = {
    'staging': [],
    'production': ['tbxwagtail@by-web-2.torchbox.com'],
}

@roles('staging')
def deploy_staging():
    pass

@roles('production')
def deploy():
    with cd('/usr/local/django/tbxwagtail/'):
        run("git pull")
        run("git submodule update")

        run("/usr/local/django/virtualenvs/tbxwagtail/bin/pip install -r requirements/production.txt")
        run("/usr/local/django/virtualenvs/tbxwagtail/bin/python manage.py syncdb --settings=tbx.settings.production --noinput")
        run("/usr/local/django/virtualenvs/tbxwagtail/bin/python manage.py migrate --settings=tbx.settings.production --noinput")
        run("/usr/local/django/virtualenvs/tbxwagtail/bin/python manage.py collectstatic --settings=tbx.settings.production --noinput")
        run("/usr/local/django/virtualenvs/tbxwagtail/bin/python manage.py compress --settings=tbx.settings.production")

    run("sudo supervisorctl restart tbxwagtail")
    #sudo("/usr/local/django/virtualenvs/tbxwagtail/bin/python manage.py update_index --settings=tbx.settings.production")

@roles('production')
def fetch_live_data():
    pass