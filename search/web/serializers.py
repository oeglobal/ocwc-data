
from rest_framework import serializers
from data.models import Course, Provider, Category


class CourseSeachResultsSerializer(serializers.ModelSerializer):
    is_member = serializers.BooleanField(source='is_member')
    source = serializers.CharField(source='provider.name')
    score = serializers.SerializerMethodField('get_score')
    link = serializers.CharField(source='linkurl')
    id = serializers.CharField(source='linkhash')
    language = serializers.SerializerMethodField('get_language')

    class Meta:
        model = Course
        fields = ('id', 'link', 'title', 'description', 'author', 'author_organization', 'language', 'is_member', 'source', 'score')

    def get_score(self, obj):
        return 0

    def get_language(self, obj):
        if obj.merlot_languages:
            return [lang.name for lang in obj.merlot_languages.all()]
        else:
            return [obj.language]


class CourseListSerializer(serializers.ModelSerializer):
    categories = serializers.RelatedField(many=True)
    language = serializers.SerializerMethodField('get_language')

    class Meta:
        model = Course
        fields = ('linkhash', 'title', 'language', 'id', 'linkurl', 'author', 'categories')

    def get_language(self, obj):
        if obj.merlot_languages:
            return [lang.name for lang in obj.merlot_languages.all()]
        else:
            return [obj.language]


class CourseSerializer(serializers.ModelSerializer):
    provider_name = serializers.CharField(source='provider.name')
    categories = serializers.RelatedField(source='merlot_categories', many=True)
    language = serializers.SerializerMethodField('get_language')

    class Meta:
        model = Course
        fields = ('linkhash', 'title', 'description', 'tags', 'provider', 'provider_name', 'language',
                  'date_published', 'id', 'linkurl', 'author', 'categories')

    def transform_categories(self, obj, value):
        cat_tree = []
        for cat in obj.merlot_categories.all():
            cat_tree.append('/'.join( ['All'] + map( unicode, cat.get_ancestors() ) + [cat.name] ) )

        return cat_tree

    def get_language(self, obj):
        if obj.merlot_languages:
            return [lang.name for lang in obj.merlot_languages.all()]
        else:
            return [obj.language]


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'name', 'external_id')


class CategoryListSerializer(serializers.ModelSerializer):
    course_count = serializers.SerializerMethodField('get_course_count')

    class Meta:
        model = Category
        fields = ('name', 'course_count')

    def __init__(self, *args, **kwargs):
        language = kwargs.pop('language', None)
        super(CategoryListSerializer, self).__init__(*args, **kwargs)

        self.language = language

    def get_course_count(self, obj):
        if self.language:
            return obj.course_set.filter(language=self.language).count()
        else:
            return obj.course_set.all().count()
