from rest_framework import serializers
from data.models import Course, Provider

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('linkhash', 'title', 'description', 'tags', 'source', 'language', 'date_published', 'id', 'linkurl', 'author')

class ProviderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Provider
		fields = ('id', 'source', 'crmid')