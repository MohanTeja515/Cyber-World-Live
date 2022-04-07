from rest_framework import serializers
from .models import Labs, LabTopic

class LabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labs
        fields = '__all__'
        lookup_field = 'lab_slug'

class LabsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labs
        fields = ('id', 'lab_title', 'lab_photos', 'lab_slug', 'lab_level', 'lab_difficulty', 'lab_area', 'lab_sections', 'lab_points_add', 'lab_points_minus')
        lookup_field = 'lab_slug'

class LabTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTopic
        fields = '__all__'
        lookup_field = 'lab_topic_slug'

class LabTopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTopic
        fields = ('id', 'lab_topic_title', 'lab_topic_slug', 'module')
        lookup_field = 'module'

