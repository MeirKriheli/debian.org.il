from django import template
from pages.models import Page

register = template.Library()


@register.simple_tag
def get_pages_in_menu():
    return Page.objects.filter(in_menu=True).order_by('id')
