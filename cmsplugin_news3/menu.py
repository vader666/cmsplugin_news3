# -*- coding: utf-8 -*-
from datetime import datetime

from django.core.urlresolvers import reverse
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu
from django.utils.translation import ugettext_lazy as _

from .models import News3
from .settings import CMSPLUGIN_NEWS3_ENABLE_DROPDOWN_MENU


__author__ = 'vader666'


class CMSLatestNews3AppMenu(CMSAttachMenu):

    name = _("News Navigation")

    def get_nodes(self, request):
        nodes = []
        if not CMSPLUGIN_NEWS3_ENABLE_DROPDOWN_MENU:
            return nodes
        try:
            years = months = days = slugs = []
            for item in News3.published.all():
                pub_date = item.pub_date

                if not pub_date.year in years:
                    years.append(pub_date.year)
                    nodes.append(NavigationNode(pub_date.year,
                        reverse('cmsplugin_news3:news3_archive_year', kwargs={'year': pub_date.year}), pub_date.year))
                    months = []

                if not pub_date.month in months:
                    months.append(pub_date.month)
                    nodes.append(NavigationNode(datetime.strftime(pub_date, '%B'),
                        reverse('cmsplugin_news3:news3_archive_month', kwargs={
                            'year': pub_date.year,
                            'month': datetime.strftime(pub_date, '%m'),
                        }), datetime.strftime(pub_date, '%m'), pub_date.year))
                    days = []

                if not pub_date.day in days:
                    days.append(pub_date.day)
                    nodes.append(NavigationNode(datetime.strftime(pub_date, '%d'),
                        reverse('cmsplugin_news3:news3_archive_day', kwargs={
                            'year': pub_date.year,
                            'month': datetime.strftime(pub_date, '%m'),
                            'day': datetime.strftime(pub_date, '%d'),
                        }), datetime.strftime(pub_date, '%d'), datetime.strftime(pub_date, '%m')))
                    slugs = []

                if not item.slug in slugs:
                    slugs.append(item.slug)
                    nodes.append(NavigationNode(
                        item.title, item.get_absolute_url(), item.pk, datetime.strftime(pub_date, '%d')))
        except:
            pass
        return nodes

menu_pool.register_menu(CMSLatestNews3AppMenu)