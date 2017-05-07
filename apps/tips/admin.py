from django.contrib import admin

from .models import Tip


@admin.register(Tip)
class TipsAdmin(admin.ModelAdmin):

    list_display = ('slug', 'title', 'create_date')
