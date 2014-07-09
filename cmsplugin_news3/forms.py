# -*- coding: utf-8 -*-
__author__ = 'vader666'

from django import forms
from cms.plugin_pool import plugin_pool
from djangocms_text_ckeditor.widgets import TextEditorWidget
from .models import News3


class News3Form(forms.ModelForm):
    class Meta:
        model = News3

    def __init__(self, *args, **kwargs):
        super(News3Form, self).__init__(*args, **kwargs)
        plugins = plugin_pool.get_text_enabled_plugins(placeholder=None, page=None)
        widget = TextEditorWidget(installed_plugins=plugins)
        self.fields['content'].widget = widget