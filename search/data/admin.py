from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
	list_display = ('title', 'language', 'provider')
	list_filter = ('language', 'provider')

class SourceAdmin(admin.ModelAdmin):
	list_display = ('id', 'provider', 'kind', 'url')
	list_filter = ('kind',)
	search_fields = ('provider__name',)

admin.site.register(Provider)
admin.site.register(Source, SourceAdmin)
admin.site.register(Course, CourseAdmin)