# -*- coding: utf-8 -*-
from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext
from .forms import News3Form
from .models import News3


__author__ = 'vader666'


class News3Admin(FrontendEditableAdminMixin, admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('slug', 'title', 'is_published', 'pub_date', 'author')
    list_filter = ('is_published', )
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title', )}
    current_user_field = 'author'
    frontend_editable_fields = ("title", "author")
    form = News3Form

    frontend_editable_fields = ("title", )

    actions = ['make_published', 'make_unpublished']

    save_as = True
    save_on_top = True

    def get_queryset(self, request):
        return News3.objects.all()

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('is_published')
        return super(News3Admin, self).get_form(request, obj, **kwargs)

    def add_view(self, request, form_url='', extra_context=None):
        self._current_user = request.user
        return super(News3Admin, self).add_view(request, form_url, extra_context)

    def save_model(self, request, obj, form, change):
        if obj.is_published and not self.user_can_publish(request.user):
            raise PermissionDenied(_('You do not have permission to save published news articles.'))
        else:
            obj.save()

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(News3Admin, self).formfield_for_dbfield(db_field, **kwargs)
        if hasattr(self, '_current_user') and db_field.name == self.current_user_field:
            field.initial = self._current_user.pk
        return field

    def user_can_publish(self, user):
        return user.has_perm('news3.can_publish')

    def make_published(self, request, queryset):
        if not self.user_can_publish(request.user):
            raise PermissionDenied(_('You do not have permission to publish news articles.'))
        else:
            rows_updated = queryset.update(is_published=True)
            self.message_user(request, ungettext('%(count)d newsitem was published',
                                                 '%(count)d newsitems where published',
                                                 rows_updated) % {'count': rows_updated})

    make_published.short_description = _('Publish selected news')

    def make_unpublished(self, request, queryset):
        if not self.user_can_publish(request.user):
            raise PermissionDenied(_('You do not have permission to unpublish news articles.'))
        else:
            rows_updated =queryset.update(is_published=False)
            self.message_user(request, ungettext('%(count)d newsitem was unpublished',
                                                 '%(count)d newsitems where unpublished',
                                                 rows_updated) % {'count': rows_updated})

    make_unpublished.short_description = _('Unpublish selected news')

admin.site.register(News3, News3Admin)