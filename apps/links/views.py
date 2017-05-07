from django.contrib.contenttypes.models import ContentType
from django.views.generic import ListView, DetailView
from taggit.models import Tag

from .models import Link


class LinksIndexView(ListView):

    model = Link
    paginate_by = 10


class LinkDetailView(DetailView):

    model = Link

    def get_object(self, queryset=None):
        link = super().get_object(queryset)
        link.hits += 1
        link.save()

        return link


class LinksByTagView(DetailView):

    model = Tag
    template_name = 'links/tag_list.html'

    def get_context_data(self, **kwargs):
        "Adds links tagged under this tag"
        context = super().get_context_data(**kwargs)

        ct = ContentType.objects.get_for_model(Link)
        context['tagged_items'] = self.object.taggit_taggeditem_items.filter(
            content_type=ct)

        return context
