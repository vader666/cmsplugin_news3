# -*- coding: utf-8 -*-
from django.views.generic.dates import MonthArchiveView, YearArchiveView, DayArchiveView, DateDetailView

from .models import News3
from .settings import CMSPLUGIN_NEWS3_PAGINATION_BY


__author__ = 'vader666'


class News3YearArchiveView(YearArchiveView):
    queryset = News3.objects.all()
    date_field = 'pub_date'
    make_object_list = True
    allow_future = True
    allow_empty = True
    paginate_by = CMSPLUGIN_NEWS3_PAGINATION_BY
    context_object_name = 'news3_list'


class News3MonthArchiveView(MonthArchiveView):
    queryset = News3.objects.all()
    date_field = 'pub_date'
    make_object_list = True
    allow_future = True
    month_format = '%m'
    paginate_by = CMSPLUGIN_NEWS3_PAGINATION_BY
    allow_empty = True
    context_object_name = 'news3_list'


class News3DayArchiveView(DayArchiveView):
    queryset = News3.objects.all()
    date_field = 'pub_date'
    make_object_list = True
    allow_future = False
    month_format = '%m'
    paginate_by = CMSPLUGIN_NEWS3_PAGINATION_BY
    allow_empty = True
    context_object_name = 'news3_list'


class News3DateDetailView(DateDetailView):
    queryset = News3.objects.all()
    date_field = 'pub_date'
    month_format = '%m'
    model = News3
    context_object_name = 'news'
