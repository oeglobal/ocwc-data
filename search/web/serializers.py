
from rest_framework import serializers
from data.models import Course, Provider, MerlotCategory, Source


class CourseSeachResultsSerializer(serializers.ModelSerializer):
    is_member = serializers.BooleanField(source='is_member')
    source = serializers.CharField(source='provider.name')
    score = serializers.SerializerMethodField('get_score')
    link = serializers.CharField(source='linkurl')
    id = serializers.CharField(source='linkhash')
    language = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'link', 'title', 'description', 'author', 'author_organization',
                  'language', 'is_member', 'source', 'score', 'merlot_id')

    def get_score(self, obj):
        return 0

    def get_language(self, obj):
        if obj.merlot_languages.exists():
            return [lang.name for lang in obj.merlot_languages.all()]
        elif obj.language:
            return [obj.language]

        return ['English']

class CourseListSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(source='merlot_categories', many=True, read_only=True)
    language = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('linkhash', 'title', 'language', 'id', 'linkurl', 'author', 'categories')

    def get_language(self, obj):
        if obj.merlot_languages.exists():
            return [lang.name for lang in obj.merlot_languages.all()]
        elif obj.language:
            return [obj.language]

        return ['English']

    def transform_categories(self, obj, value):
        cat_tree = []
        for cat in obj.merlot_categories.all():
            cat_tree.append('/'.join( ['All'] + map( unicode, cat.get_ancestors() ) + [cat.name] ) )

        return cat_tree

class CourseSerializer(serializers.ModelSerializer):
    provider_name = serializers.CharField(source='provider.name')
    categories = serializers.SerializerMethodField('transform_categories', read_only=True)
    categories_ids = serializers.PrimaryKeyRelatedField(source='merlot_categories', many=True, read_only=True)
    language = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('linkhash', 'title', 'description', 'tags', 'provider', 'provider_name', 'language',
                  'date_published', 'id', 'linkurl', 'author', 'categories', 'merlot_id', 'categories_ids')

    def transform_categories(self, obj):
        cat_tree = []
        for cat in obj.merlot_categories.all():
            cat_tree.append('/'.join( ['All'] + map( unicode, cat.get_ancestors() ) + [cat.name] ) )

        return cat_tree

    def get_language(self, obj):
        if obj.merlot_languages.exists():
            return [lang.name for lang in obj.merlot_languages.all()]
        else:
            return [obj.language]


class ProviderSerializer(serializers.ModelSerializer):
    course_count_merlot = serializers.SerializerMethodField('get_merlot_count')
    course_count = serializers.SerializerMethodField('get_count')

    class Meta:
        model = Provider
        fields = ('id', 'name', 'external_id', 'course_count_merlot', 'course_count')

    def get_merlot_count(self, obj):
        return obj.get_merlot_count()

    def get_count(self, obj):
        return Course.objects.filter(provider=obj).count()


class CategoryListSerializer(serializers.ModelSerializer):
    course_count = serializers.SerializerMethodField()
    category_id = serializers.CharField(source="merlot_id")

    class Meta:
        model = MerlotCategory
        fields = ('name', 'category_id', 'course_count')

    def __init__(self, *args, **kwargs):
        language = kwargs.pop('language', None)
        super(CategoryListSerializer, self).__init__(*args, **kwargs)

        self.language = language

    def get_course_count(self, obj):
        if hasattr(obj, 'o_count'):
            return obj.o_count

        return 0

class SourceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='provider.name', read_only=True)
    merlot_missing = serializers.CharField(source='get_merlot_missing', read_only=True)
    course_count = serializers.CharField(source='get_total_count', read_only=True)
    courses = serializers.PrimaryKeyRelatedField(source='course_set', many=True, read_only=True)

    class Meta:
        model = Source
        fields = ('id', 'name', 'kind', 'merlot_missing', 'course_count', 'courses')

class CourseRetrieveUpdateSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source='source.provider.name', read_only=True)
    merlot_detail_url = serializers.CharField(read_only=True)
    categories = serializers.PrimaryKeyRelatedField(source='merlot_categories', many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('source', 'id', 'title', 'description', 'language',
                    'merlot_present', 'merlot_detail_url', 'categories')
        read_only_fields = ('merlot_present',)

class CategoryListSerializerAPI2(serializers.ModelSerializer):
    merlot_id = serializers.CharField()

    class Meta:
        model = MerlotCategory
        fields = ('id', 'name', 'merlot_id')

class CategoryFlatListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    merlot_id = serializers.CharField()

    class Meta:
        model = MerlotCategory
        fields = ('id', 'name', 'merlot_id')

    def get_name(self, obj):
        return ' / '.join( map( unicode, obj.get_ancestors() ) + [obj.name] )
