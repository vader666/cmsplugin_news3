# -*- coding: utf-8 -*-
from cms.models import CMSPlugin
import datetime
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField

__author__ = 'vader666'

from django.db import models


class PublishedNewsManager(models.Manager):
    """
        Filters out all unpublished and items with a publication date in the future
    """
    def get_query_set(self):
        return super(PublishedNewsManager, self).get_query_set() \
            .filter(is_published=True) \
            .filter(pub_date__lte=datetime.datetime.now())


class News3(CMSPlugin):
    """
        News model
    """
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'),
                            unique_for_date='pub_date',
                            help_text=_('A slug is a short name which uniquely identifies the news item for this day'))
    author = models.ForeignKey(User, blank=True, null=True)
    excerpt = models.TextField(_('Excerpt'), blank=True)
    content = models.TextField(_('Content'), blank=True)
    photo = FilerImageField(blank=True, null=True, help_text=_('Optional. Image for news article.'), on_delete=models.SET_NULL)
    is_published = models.BooleanField(_('Published'), default=False)
    pub_date = models.DateField(_('Publication date'), default=datetime.datetime.now())
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    published = PublishedNewsManager()
    objects = models.Manager()

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        app_label = 'cmsplugin_news3'
        ordering = ('-pub_date',)
        permissions = (
            ('can_publish', _('Can publish/unpublish news article')),
        )

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('cmsplugin_news3:news3_detail', (), {
                'year': self.pub_date.strftime("%Y"),
                'month': self.pub_date.strftime("%m"),
                'day': self.pub_date.strftime("%d"),
                'slug': self.slug,
            })


class LatestNews3(CMSPlugin):
    """
        Model for the settings when using the latest news cms plugin
    """
    limit = models.PositiveIntegerField(_('Numbers of news items to show'), default=3,
                                        help_text=_('Limits the number of items that will be displayed'))