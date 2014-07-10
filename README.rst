===============
cmsplugin-news3
===============

Description: A news application and plugin for Django-CMS 3

Based on https://github.com/wildfish/cmsplugin_news

This if first version of my first plugin

Supported Django versions:
* Django 1.6

Supported Django-CMS versions:
* Django-CMS 3.x

Requirements 
------------
* django-cms
* django-filer
* easy-thumbnauls

Installation
------------
* ``pip install -e git+https://github.com/vader666/cmsplugin_news3.git#egg=cmsplugin_news3``
* add ``filer``, ``easy_thumbnails``, ``cmsplugin_news3`` to INSTALLED_APPS
* run ``./manage.py syncdb`` and ``./manage.py migrate``
* restart server 

Usage
-----
* Create a page in cms, in the 'advanced settings' section of the admin for that page, for 'Navigation extenders' select 'News Navigation' and for application select 'Last News'.
* Befor using the plugin, **make sure that the cms page was created!** The 'Last News' plugin you can insert into placeholder on any page.
* Create a propper tepmplates for your site.

Settings
--------
* Boolean CMSPLUGIN_NEWS3_DISABLE_LATEST_NEWS Disable Latest News Plugin, default - enabled
* Integer CMSPLUGIN_NEWS3_PAGINATION_BY Pagination at News application, default - 12
* Boolean CMSPLUGIN_NEWS3_ENABLE_DROPDOWN_MENU Enable drop down meny for News applicatio, default - disabled
