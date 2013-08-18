from rest_framework import serializers
from joomla.models import JosOcwCourses, CfGetorgs

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = JosOcwCourses
		fields = ('linkhash', 'title', 'description', 'tags', 'source', 'language', 'date_published', 'id', 'linkurl', 'author', 'crmid')

class SourceSerializer(serializers.ModelSerializer):
	class Meta:
		model = CfGetorgs
		fields = ('id', 'source', 'crmid')