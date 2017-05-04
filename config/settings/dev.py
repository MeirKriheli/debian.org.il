# -*- coding: utf-8 -*-
"""
Django developer settings

- debug mode true
- django-debug-toolbar

"""

from .common import *  # noqa

# ------------------------------------------------------------------------------
# DEBUG
# ------------------------------------------------------------------------------

DEBUG = env.bool('DJANGO_DEBUG', default=True)

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


# ------------------------------------------------------------------------------
# SECRET CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.`
SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!')

# ------------------------------------------------------------------------------
# STATIC
# ------------------------------------------------------------------------------

STATICFILES_DIRS = (
    str(ROOT_DIR.path('assets')),
)

# ------------------------------------------------------------------------------
# DJANGO DEBUG TOOLBAR
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.org/en/1.3.2/
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# ------------------------------------------------------------------------------
# TESTING
# ------------------------------------------------------------------------------

# this app is used for site wide functional testing
INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# running tests will also run coverage + only include the apps listed below.
# inclusive will scan all files in working dir to see which are not being covered
NOSE_ARGS = [
    '--verbosity=2',
    '--with-coverage',
    # '--cover-package=add packages here',
    '--cover-inclusive',
]
