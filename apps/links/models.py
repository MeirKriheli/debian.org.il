from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager

LINK_LANGUAGES = (
    ('he', _('Hebrew')),
    ('en', _('English')),
)


class Link(models.Model):
    """Debian related external links"""

    slug = models.SlugField(_('Link for the url'))
    url = models.URLField(_('Destination URL'))
    create_date = models.DateTimeField(_('Added at'), auto_now_add=True,
                                       blank=True, db_index=True)
    title = models.CharField(_('Title'), max_length=100)
    description = RichTextField(_('Description'), blank=True)
    hits = models.IntegerField(_('Hits'), editable=False, null=True,
                               db_index=True, default=0)
    language = models.CharField(_('Link Language'), max_length=5, blank=True,
                                null=True, choices=LINK_LANGUAGES)
    tags = TaggableManager()

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')
        ordering = ('-create_date',)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        # FIXME use reverse and url namespace
        return "/links/%s" % self.slug
