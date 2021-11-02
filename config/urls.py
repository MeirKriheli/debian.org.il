# -*- coding: utf-8 -*-
"""
debian.org.il URL Configuration
"""
from django.conf import settings
from django.urls import include, path
from django.contrib import admin


admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        r'links/',
        include('links.urls', namespace='links')),
    path(
        r'tips/',
        include('tips.urls', namespace='tips')),
    path(
        r'',
        include('pages.urls', namespace='pages')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
