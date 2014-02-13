# -*- coding: utf-8 -*-
from django.core.exceptions import PermissionDenied

from vanilla import ListView, DetailView, TemplateView, RedirectView, UpdateView, CreateView, FormView

from data.models import Course, Provider, Source, Category

from ..forms import CourseModelForm

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

class CourseDetailView(DetailView):
    model = Course
    template_name = 'web/course_detail.html'

class CourseAddView(FormView):
    model = Course
    form_class = CourseModelForm
    template_name = "web/course_form.html"

    def get_form(self, data=None, files=None, **kwargs):
        edit_key = self.kwargs.pop('edit_key')
        
        if Source.objects.filter(edit_key=edit_key).exists():
            kwargs['edit_key'] = edit_key
        else:
            raise PermissionDenied

        return self.form_class(data, files, **kwargs)
