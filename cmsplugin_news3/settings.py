# -*- coding: utf-8 -*-
from django.conf import settings as django_settings

__author__ = 'vader666'


"""
    Disable Latest news plugin
    Default false
"""
CMSPLUGIN_NEWS3_DISABLE_LATEST_NEWS = getattr(django_settings, 'CMSPLUGIN_NEWS3_DISABLE_LATEST_NEWS', False)

"""
    Setting for Pagination
    Default 12

"""
CMSPLUGIN_NEWS3_PAGINATION_BY = getattr(django_settings, 'CMSPLUGIN_NEWS3_PAGINATION_BY', 12)

"""
    Setting for drop down menu
    Default false
"""
CMSPLUGIN_NEWS3_ENABLE_DROPDOWN_MENU = getattr(django_settings, 'CMSPLUGIN_NEWS3_ENABLE_DROPDOWN_MENU', False)