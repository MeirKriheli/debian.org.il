from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

from .models import Page


class PageView(DetailView):

    model = Page

    def get_object(self, queryset=None):

        slug = self.kwargs.get('slug')
        if not slug:
            slug = 'index'
        return get_object_or_404(self.get_queryset(), slug=slug)
