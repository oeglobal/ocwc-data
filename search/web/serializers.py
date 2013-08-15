from rest_framework import serializers
from joomla.models import JosOcwCourses

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = JosOcwCourses
		fields = ('linkhash', 'title', 'description', 'tags', 'source', 'language', 'date_published', 'id')