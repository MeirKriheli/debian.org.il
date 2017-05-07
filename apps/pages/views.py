from django.views.generic import DetailView

from .models import Page


class PageView(DetailView):

    model = Page

    def get_object(self, queryset=None):

        slug = self.kwargs.get('slug')
        if not slug:
            slug = 'index'
        return self.get_queryset().get(slug=slug)
