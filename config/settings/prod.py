# -*- coding: utf-8 -*-
"""
Production settings
"""

from __future__ import absolute_import, unicode_literals

from .common import *  # noqa


# ------------------------------------------------------------------------------
# SECRET CONFIGURATION
# ------------------------------------------------------------------------------

SECRET_KEY = env("DJANGO_SECRET_KEY")

# ------------------------------------------------------------------------------
# STATIC CONFIGURATION
# ------------------------------------------------------------------------------

STATIC_ROOT = env('DJANGO_STATIC_ROOT')

# ------------------------------------------------------------------------------
# SITE CONFIGURATION
# ------------------------------------------------------------------------------

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['debian.org.il'])

# Custom Admin URL, use {% url 'admin:index' %}
ADMIN_URL = env('DJANGO_ADMIN_URL')
