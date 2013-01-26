from django.contrib import admin
from web.models import *


class CourseFeedAdmin(admin.ModelAdmin):
    list_display = ('source', 'crmid', 'language','last_index', 'enabled', 'reviewed')
    list_filter = ('enabled', 'reviewed')

class CourseAdmin(admin.ModelAdmin):
	list_display = ('source', 'title', 'retrieved')

admin.site.register(CourseFeed, CourseFeedAdmin)
admin.site.register(Course, CourseAdmin)
