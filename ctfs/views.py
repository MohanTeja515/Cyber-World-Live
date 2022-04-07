from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CTFFiles, CTFs, CTFsTopic
from .serializers import CTFsFilesSerializer, CTFsPageSerializer, CTFsTopicSerializer, CTFsListSerializer, CTFSerializer, CTFsAnswer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CTFsPageListView(ListAPIView):
    queryset = CTFs.objects.order_by('-ctfs_date_created')
    serializer_class = CTFsPageSerializer
    lookup_field = 'ctfs_slug'
    permission_classes = (permissions.AllowAny, )

class CTFsDetailView(RetrieveAPIView):
    queryset = CTFs.objects.order_by('-ctfs_date_created')
    serializer_class = CTFSerializer
    lookup_field = 'ctfs_slug'
    permission_classes = (permissions.AllowAny, )
    
class CTFsTopicDetailView(RetrieveAPIView):
    queryset = CTFsTopic.objects.all()
    serializer_class = CTFsTopicSerializer
    lookup_field = 'ctfs_topic_slug'
    permission_classes = (permissions.AllowAny, )

class CTFsTopicListView(ListAPIView):
    model = CTFsTopic
    serializer_class = CTFsListSerializer
    lookup_field = 'module'
    permission_classes = (permissions.AllowAny, )
    def get_queryset(self):
        module = self.kwargs['module']
        queryset = self.model.objects.filter(module=module)
        return queryset.all()

class SearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, pk):
        queryset = CTFsTopic.objects.get(id=pk)
        data = self.request.data
        model = CTFsTopic
        data = self.request.data
        flag = data['flag']
        serializer = CTFsAnswer(queryset)
        if flag == serializer.data["ctfs_topic_answer"]:
            return Response("True")
        else:
            return Response("False")

class CTFsFileView(ListAPIView):
    model = CTFFiles
    serializer_class = CTFsFilesSerializer
    lookup_field = 'topic'
    permission_classes = (permissions.AllowAny, )
    def get_queryset(self):
        module = self.kwargs['topic']
        queryset = self.model.objects.filter(topic=module)
        return queryset.all()




