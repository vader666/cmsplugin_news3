# -*- coding: utf-8 -*-
from cms.toolbar.items import SubMenu
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

__author__ = 'vader666'


@toolbar_pool.register
class News3Toolbar(CMSToolbar):
    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu('news3_menu', _('News'))

        admin_menu.add_sideframe_item(_('News list'), url=reverse('admin:cmsplugin_news3_news3_changelist'))
        admin_menu.add_sideframe_item(_('Add news'), url=reverse('admin:cmsplugin_news3_news3_add'))
