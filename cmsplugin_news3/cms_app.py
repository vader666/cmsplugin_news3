# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from cmsplugin_news3.menu import CMSLatestNews3AppMenu

__author__ = 'vader666'


class News3Apphook(CMSApp):
    name = _('Latest News')
    urls = ['cmsplugin_news3.urls']
    menus = [CMSLatestNews3AppMenu]
    app_name = 'cmsplugin_news3'

apphook_pool.register(News3Apphook)