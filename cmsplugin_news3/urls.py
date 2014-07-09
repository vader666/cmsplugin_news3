# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic.dates import ArchiveIndexView

from .view import *
from .models import News3
from .settings import CMSPLUGIN_NEWS3_PAGINATION_BY


__author__ = 'vader666'


urlpatterns = patterns('',
    url(r'^$',
        ArchiveIndexView.as_view(
        model=News3,
        date_field='pub_date',
        allow_empty=True,
        paginate_by=CMSPLUGIN_NEWS3_PAGINATION_BY,),
        name='news3_archive'),
    url(r'^(?P<year>\d{4})/$',
        News3YearArchiveView.as_view(), name='news3_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        News3MonthArchiveView.as_view(), name='news3_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        News3DayArchiveView.as_view(), name='news3_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        News3DateDetailView.as_view(), name='news3_detail'),
)