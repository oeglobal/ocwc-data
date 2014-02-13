# -*- coding: utf-8 -*-
from django import forms

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field, Div, HTML

from data.models import Course, Source

class CourseModelForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		if kwargs.get('instance'):
			pass
		else:
			edit_key = kwargs.pop('edit_key')
			source = Source.objects.get(edit_key=edit_key)
			
			self.base_fields['source'].initial = source.id
			self.base_fields['source'].widget = forms.HiddenInput()

		super(CourseModelForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Course
		fields = ('title', 'linkurl', 'source', 'description', 'language', 'author', 'categories',)