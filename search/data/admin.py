from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
	list_display = ('title', 'language')
	list_filter = ('language',)

admin.site.register(Provider)
admin.site.register(Source)
admin.site.register(Course, CourseAdmin)