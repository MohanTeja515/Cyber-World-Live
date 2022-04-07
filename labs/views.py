from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Labs, LabTopic
from .serializers import LabsSerializer, LabsPageSerializer, LabTopicSerializer, LabTopicListSerializer

class LabsPageListView(ListAPIView):
    queryset = Labs.objects.order_by('lab_level')
    serializer_class = LabsPageSerializer
    lookup_field = 'labs_slug'
    permission_classes = (permissions.AllowAny, )

class LabsDetailView(RetrieveAPIView):
    queryset = Labs.objects.order_by('lab_level')
    serializer_class = LabsSerializer
    lookup_field = 'lab_slug'
    permission_classes = (permissions.AllowAny, )
    
class LabTopicDetailView(RetrieveAPIView):
    queryset = LabTopic.objects.order_by('-lab_topic_date_created')
    serializer_class = LabTopicSerializer
    lookup_field = 'lab_topic_slug'
    permission_classes = (permissions.AllowAny, )


class LabTopicListView(ListAPIView):
    model = LabTopic
    serializer_class = LabTopicListSerializer
    lookup_field = 'module'
    permission_classes = (permissions.AllowAny, )
    def get_queryset(self):
        module = self.kwargs['module']
        queryset = self.model.objects.filter(module=module)
        return queryset.all()



