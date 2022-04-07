from django.urls import path
from .views import ModuleDetailView, ModulePageListView, TopicDetailView, TopicListView

urlpatterns = [
    path('', ModulePageListView.as_view()),
    path('<module_slug>/', ModuleDetailView.as_view()),
    path('<module>/topics/', TopicListView.as_view()),
    path('topic/<topic_slug>/', TopicDetailView.as_view()),
]