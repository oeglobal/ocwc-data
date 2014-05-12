# -*- coding: utf-8 -*-
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from vanilla import ListView, DetailView, FormView

from data.models import Course, Source

from ..forms import CourseModelForm


class SourceCourseListView(ListView):
    model = Course
    template_name = 'web/source_course_list.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return self.model.objects.filter(source=pk).order_by('id')

    def get_context_data(self, **kwargs):
        context = super(SourceCourseListView, self).get_context_data(**kwargs)
        context['source'] = Source.objects.get(pk=self.kwargs.get('pk'))
        
        return context


class CourseActionMixin(object):
    pass


class CourseDetailView(DetailView):
    model = Course
    template_name = 'web/course_detail.html'


class CourseFormAddView(CourseActionMixin, FormView):
    model = Course
    form_class = CourseModelForm
    template_name = "web/course_form.html"

    def dispatch(self, request, *args, **kwargs):
        edit_key = kwargs.pop('edit_key')
        
        try:
            self.source = Source.objects.get(edit_key=edit_key)
        except Source.DoesNotExist:
            raise PermissionDenied

        return super(CourseFormAddView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CourseFormAddView, self).get_context_data(**kwargs)
        context['source'] = self.source

        return context

    def get_form(self, data=None, files=None, **kwargs):
        kwargs['source'] = self.source
        return self.form_class(data, files, **kwargs)

    def form_valid(self, form):
        cleaned_data = form.cleaned_data

        cleaned_data['source'] = self.source
        cleaned_data['provider'] = self.source.provider

        categories = cleaned_data.pop('categories')

        course = Course(**cleaned_data)
        course.save()

        for cat in categories:
            course.categories.add(cat)

        return redirect(self.source.get_absolute_url())


class CourseFormEditView(CourseActionMixin, FormView):
    model = Course
    form_class = CourseModelForm
    template_name = "web/course_form.html"

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.pop('pk')
        self.instance = Course.objects.get(pk=pk)

        return super(CourseFormEditView, self).dispatch(request, *args, **kwargs)

    def get_form(self, data=None, files=None, **kwargs):
        kwargs['instance'] = self.instance
        return self.form_class(data, files, **kwargs)

    def form_valid(self, form):
        course = self.instance

        cleaned_data = form.cleaned_data

        cleaned_data['source'] = course.source
        cleaned_data['provider'] = course.source.provider

        categories = cleaned_data.pop('categories')

        for key in cleaned_data:
            setattr(course, key, cleaned_data.get(key))
        course.save(update_linkhash=True)

        course.categories.clear()
        for cat in categories:
            course.categories.add(cat)

        return redirect(reverse('dashboard:course-view', kwargs={'linkhash': course.linkhash}))
