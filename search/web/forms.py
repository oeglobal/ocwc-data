# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Submit, Layout, Field, Row, HTML, Div

import django_select2

from data.models import Course, LANGUAGE_CHOICES, PRIMARY_AUDIENCE_CHOICES, YES_NO_UNSURE_CHOICES, CC_DERIV_CHOICES


class CourseModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            self.instance = kwargs.get('instance')
        else:
            source = kwargs.pop('source')
            self.base_fields['source'].initial = source.id
            self.base_fields['language'].initial = 'English'
            self.instance = None

        self.base_fields['source'].widget = forms.HiddenInput()

        self.base_fields['merlot_categories'].widget = django_select2.widgets.Select2MultipleWidget()
        self.base_fields['merlot_categories'].help_text = "Press Esc key to close the selection box after you've selected all relevant categories."

        self.base_fields['language'].widget = django_select2.widgets.Select2Widget(choices=LANGUAGE_CHOICES)
        self.base_fields['tags'].help_text = "Separate tags with commas"

        self.base_fields['audience'].widget = forms.RadioSelect(choices=PRIMARY_AUDIENCE_CHOICES)
        self.base_fields['creative_commons'].widget = forms.RadioSelect(choices=YES_NO_UNSURE_CHOICES)
        self.base_fields['creative_commons_commercial'].widget = forms.RadioSelect(choices=YES_NO_UNSURE_CHOICES)
        self.base_fields['creative_commons_derivatives'].widget = forms.RadioSelect(choices=CC_DERIV_CHOICES)

        self.helper = FormHelper()
        self.helper.form_action = '.'

        self.helper.layout = Layout(
            Row(
                Field('merlot_ignore'),
                Field('title'),
                Field('linkurl'),
                Field('description'),
                Field('language'),
                Field('content_medium'),
                Field('author'),
                Field('tags'),
            ),
        )

        if self.instance and self.instance.categories.count():
            self.helper.layout.append(Layout(
                Row(
                    HTML("<h4>Legacy categories:</h4>"),
                    HTML(
                    """ {%load mptt_tags %}
                        <p>
                        {% for node in course.categories.all %}
                        {{ node.get_ancestors|tree_path:" > " }} > {{ node }}<br />
                        {% endfor %}
                        </p>
                    """)
                ))
            )

        self.helper.layout.append(Layout(
            Row(
                HTML("<a href='http://www.merlot.org/merlot/categories.htm' target='_blank'>Full Merlot Categories list</a>"),
                Field('merlot_categories'),
            )
        ))

        self.helper.layout.append(Layout(
            Row(
                Field('image_url'),
                Div(Field('audience'),
                    css_class="small-4 columns"),
                Div(Field('creative_commons'),
                    css_class="small-4 columns"),
                Div(Field('creative_commons_commercial'),
                    css_class="small-4 columns"),
                Div(Field('creative_commons_derivatives'),
                    css_class="small-8 columns left"),
            )
        ))

        self.helper.layout.append(
            Row(
                Submit('Save', 'save'),
            css_class="buttons")
        )

        super(CourseModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Course
        fields = ('title', 'linkurl', 'source', 'description', 'language', 'author', 'merlot_categories',
                  'tags', 'content_medium', 'merlot_ignore',
                  'image_url', 'audience',
                  'creative_commons', 'creative_commons_commercial', 'creative_commons_derivatives',)
