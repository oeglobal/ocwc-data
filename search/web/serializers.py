from rest_framework import serializers
from data.models import Course, Provider

class CourseListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('linkhash', 'title', 'language', 'id', 'linkurl', 'author')

class CourseSerializer(serializers.ModelSerializer):
	provider_name = serializers.CharField(source='provider.name')
	class Meta:
		model = Course
		fields = ('linkhash', 'title', 'description', 'tags', 'provider', 'provider_name', 'language', 
				  'date_published', 'id', 'linkurl', 'author')

class ProviderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Provider
		fields = ('id', 'name', 'external_id')