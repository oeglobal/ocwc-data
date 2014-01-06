# -*- coding: utf-8 -*-
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

class CourseAdmin(admin.ModelAdmin):
	list_display = ('title', 'language', 'provider', 'calais_socialtags', 'calais_topics')
	list_filter = ('language', 'provider')
	search_fields = ('title', 'description')

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

admin.site.register(Provider, ProviderAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)