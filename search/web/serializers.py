from rest_framework import serializers
from data.models import Course, Provider, Category

class CourseListSerializer(serializers.ModelSerializer):
	categories = serializers.RelatedField(many=True)
	
	class Meta:
		model = Course
		fields = ('linkhash', 'title', 'language', 'id', 'linkurl', 'author', 'categories')

class CourseSerializer(serializers.ModelSerializer):
	provider_name = serializers.CharField(source='provider.name')
	categories = serializers.RelatedField(many=True)

	class Meta:
		model = Course
		fields = ('linkhash', 'title', 'description', 'tags', 'provider', 'provider_name', 'language', 
				  'date_published', 'id', 'linkurl', 'author', 'categories')

class ProviderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Provider
		fields = ('id', 'name', 'external_id')

class CategoryListSerializer(serializers.ModelSerializer):
	course_count = serializers.SerializerMethodField('get_course_count')

	class Meta:
		model = Category
		fields = ('name','course_count')

	def __init__(self, *args, **kwargs):
		language = kwargs.pop('language', None)
		super(CategoryListSerializer, self).__init__(*args, **kwargs)

		self.language = language

	def get_course_count(self, obj):
		if self.language:
			return obj.course_set.filter(language=self.language).count()
		else:
			return obj.course_set.all().count()