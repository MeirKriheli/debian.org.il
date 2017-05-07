from django.contrib import admin

from .models import Link


@admin.register(Link)
class LinksAdmin(admin.ModelAdmin):

    list_display = ('slug', 'url', 'create_date')
