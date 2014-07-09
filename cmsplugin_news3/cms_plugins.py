# -*- coding: utf-8 -*-
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from .models import News3, LatestNews3
from .settings import CMSPLUGIN_NEWS3_DISABLE_LATEST_NEWS

__author__ = 'vader666'



class CMSLatestNews3Plugin(CMSPluginBase):
    name = _('Latest news')
    model = LatestNews3
    render_template = "cmsplugin_news3/news3_latest.html"
    cache = False

    def render(self, context, instance, placeholder):
        latest = News3.published.all()[:instance.limit]
        context.update({
            'instance': instance,
            'latest': latest,
            'placeholder': placeholder,
        })
        return context

if not CMSPLUGIN_NEWS3_DISABLE_LATEST_NEWS:
    plugin_pool.register_plugin(CMSLatestNews3Plugin)