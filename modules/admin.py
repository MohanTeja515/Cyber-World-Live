from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Module, Topic

class ModuleAdmin(SummernoteModelAdmin):
    exclude = ('module_slug', )
    list_display = ('id', 'module_title', 'module_level', 'module_date_created')
    list_display_links = ('id', 'module_title')
    search_fields = ('module_title', )
    list_per_page = 25
    summernote_fields = ('module_content', 'module_description')

class TopicAdmin(SummernoteModelAdmin):
    exclude = ('topic_slug', )
    list_display = ('id', 'topic_title', 'topic_number', 'topic_date_created')
    list_display_links = ('id', 'topic_title')
    search_fields = ('topic_title', )
    list_per_page = 25
    summernote_fields = ('topic_content', 'topic_description' )

admin.site.register(Topic, TopicAdmin)

admin.site.register(Module, ModuleAdmin)