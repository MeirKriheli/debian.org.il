from ckeditor.fields import RichTextField
from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Page(models.Model):
    slug = models.SlugField(_('Link for the url'))
    title = models.CharField(_('Title'), max_length=100)
    content = RichTextField(_('Content'))
    in_menu = models.BooleanField(_('Show in menu'), default=True)

    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        """ returns url for the page. index is a special case """
        if self.slug == 'index':
            return reverse('pages:index')
        else:
            return reverse('pages:page', kwargs={'slug': self.slug})
