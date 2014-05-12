# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Submit, Layout, Field, Div, HTML, Row

import django_select2

from data.models import Course, Source, LANGUAGE_CHOICES

class CourseModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            pass
        else:
            source = kwargs.pop('source')
            self.base_fields['source'].initial = source.id
            self.base_fields['source'].widget = forms.HiddenInput()
            self.base_fields['language'].initial = 'English'

        self.base_fields['categories'].widget = django_select2.widgets.Select2MultipleWidget()
        self.base_fields['categories'].help_text = "Press Esc key to close the selection box after you've selected all relevant categories."

        self.base_fields['language'].widget = django_select2.widgets.Select2Widget(choices=LANGUAGE_CHOICES)
        self.base_fields['tags'].help_text = "Separate tags with commas"

        self.helper = FormHelper()
        self.helper.form_action = '.'

        self.helper.layout = Layout(
            Row(
                Field('title'),
                Field('linkurl'),
                Field('description'),
                Field('language'),
                Field('content_medium'),
                Field('author'),
                Field('tags'),
                Field('categories'),
            ),
            Row(
                Submit('Save', 'save'),
            css_class="buttons")
        )

        super(CourseModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Course
        fields = ('title', 'linkurl', 'source', 'description', 'language', 'author', 'categories', 'tags', 'content_medium')