from django.urls import path
from .views import LabTopicListView, LabsDetailView, LabsPageListView, LabTopicDetailView

urlpatterns = [
    path('', LabsPageListView.as_view()),
    path('<lab_slug>/', LabsDetailView.as_view()),
    path('lab-topic/<lab_topic_slug>/', LabTopicDetailView.as_view()),
    path('<module>/practicals/', LabTopicListView.as_view()),
]