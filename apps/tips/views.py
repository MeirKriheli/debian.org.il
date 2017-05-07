from django.contrib.contenttypes.models import ContentType
from django.views.generic import ListView, DetailView
from taggit.models import Tag

from .models import Tip


class TipsIndexView(ListView):

    model = Tip
    paginate_by = 10


class TipDetailView(DetailView):

    model = Tip

    def get_object(self, queryset=None):
        tip = super().get_object(queryset)
        tip.hits += 1
        tip.save()

        return tip


class TipsByTagView(DetailView):

    model = Tag
    template_name = 'tips/tag_list.html'

    def get_context_data(self, **kwargs):
        "Adds tips tagged under this tag"
        context = super().get_context_data(**kwargs)

        ct = ContentType.objects.get_for_model(Tip)
        context['tagged_items'] = self.object.taggit_taggeditem_items.filter(
            content_type=ct)

        return context
