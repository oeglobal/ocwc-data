# -*- coding: utf-8 -*-
from vanilla import ListView, DetailView, TemplateView, RedirectView, UpdateView, CreateView, FormView

from data.models import Course, Provider, Source, Category

class SourceCourseListView(ListView):
	model = Course
	template_name = 'web/source_course_list.html'

	def get_queryset(self):
		pk = self.kwargs.get('pk')
		return self.model.objects.filter(source=pk)

	def get_context_data(self, **kwargs):
		context = super(SourceCourseListView, self).get_context_data(**kwargs)
		context['source'] = Source.objects.get(pk=self.kwargs.get('pk'))
		
		return context
