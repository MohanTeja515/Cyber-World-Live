from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Module, Topic
from .serializers import ModuleSerializer, ModulePageSerializer, TopicSerializer, TopicListSerializer


class ModulePageListView(ListAPIView):
    queryset = Module.objects.order_by('module_level')
    serializer_class = ModulePageSerializer
    lookup_field = 'module_slug'
    permission_classes = (permissions.AllowAny, )

class ModuleDetailView(RetrieveAPIView):
    queryset = Module.objects.order_by('module_level')
    serializer_class = ModuleSerializer
    lookup_field = 'module_slug'
    permission_classes = (permissions.AllowAny, )

class TopicListView(ListAPIView):
    model = Topic
    serializer_class = TopicListSerializer
    lookup_field = 'module'
    permission_classes = (permissions.AllowAny, )
    def get_queryset(self):
        module = self.kwargs['module']
        queryset = self.model.objects.filter(module=module)
        return queryset.all()
    
class TopicDetailView(RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'topic_slug'
    permission_classes = (permissions.AllowAny, )





