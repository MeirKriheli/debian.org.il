# -*- coding: utf-8 -*-
"""
debian.org.il URL Configuration
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(
        r'^links/',
        include('links.urls', namespace='links')),
    url(
        r'^tips/',
        include('tips.urls', namespace='tips')),
    url(
        r'^',
        include('pages.urls', namespace='pages')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
