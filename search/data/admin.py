# -*- coding: utf-8 -*-
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'provider', 'merlot_present', 'is_404')
    list_filter = ('language', 'provider', 'merlot_present', 'is_404')
    search_fields = ('title', 'description', 'linkurl')


class SourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'provider', 'kind', 'url')
    list_filter = ('kind',)
    search_fields = ('provider__name',)


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'external_id', 'active')
    search_fields = ('name',)


class MerlotCategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent', 'merlot_id')
    search_fields = ('name', 'merlot_id')
    list_per_page = 1200

admin.site.register(Provider, ProviderAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MerlotCategory, MerlotCategoryAdmin)
