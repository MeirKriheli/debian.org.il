from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TipsConfig(AppConfig):
    name = 'tips'
    verbose_name = _('Tips')
