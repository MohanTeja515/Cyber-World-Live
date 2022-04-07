from rest_framework import serializers
from .models import CTFFiles, CTFs, CTFsTopic

class CTFSerializer(serializers.ModelSerializer):
    class Meta:
        model = CTFs
        fields = '__all__'
        lookup_field = 'ctfs_slug'

class CTFsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CTFs
        fields = ('id', 'ctfs_title', 'ctfs_photos', 'ctfs_slug', 'ctfs_level', 'ctfs_difficulty', 'ctfs_area', 'ctfs_sections', 'ctfs_points_add', 'ctfs_points_minus')
        lookup_field = 'ctfs_slug'

class CTFsTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CTFsTopic
        fields = '__all__'
        exlude = ('ctfs_topic_answer', )
        lookup_field = 'ctfs_topic_slug'

class CTFsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CTFsTopic
        fields = ('id', 'ctfs_topic_title', 'ctfs_topic_slug', 'module')
        lookup_field = 'module'

class CTFsAnswer(serializers.ModelSerializer):
    class Meta:
        model = CTFsTopic
        fields = ('id', 'ctfs_topic_answer', 'ctfs_topic_slug' )
        lookup_field = 'id'

class CTFsFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CTFFiles
        fields = '__all__'
        lookup_field = 'topic'