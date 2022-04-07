from rest_framework import serializers
from .models import Module, Topic

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
        lookup_field = 'module_slug'

class ModulePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id', 'module_title', 'module_photos', 'module_slug', 'module_level', 'module_difficulty', 'module_area', 'module_sections', 'module_points_add', 'module_points_minus')
        lookup_field = 'module_slug'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        lookup_field = 'topic_slug'

class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'topic_title', 'topic_slug', 'module')
        lookup_field = 'module'
