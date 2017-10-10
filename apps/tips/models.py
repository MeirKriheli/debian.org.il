from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager


class Tip(models.Model):

    slug = models.SlugField(_('Link for the url'))
    title = models.CharField(_('Title'), max_length=100)
    content = RichTextField(_('Content'))
    create_date = models.DateTimeField(_('Added at'), auto_now_add=True,
                                       blank=True, db_index=True)
    contributor = models.CharField(_('Contriuted by'), max_length=100,
                                   blank=True, null=True)
    hits = models.IntegerField(_('Hits'), editable=False, null=True,
                               db_index=True, default=0)
    pending = models.BooleanField(_('Draft'), default=False, db_index=True)
    tags = TaggableManager()

    class Meta:
        verbose_name = _('Tip')
        verbose_name_plural = _('Tips')
        ordering = ('-create_date',)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('tips:tip', kwargs={'slug': self.slug})
