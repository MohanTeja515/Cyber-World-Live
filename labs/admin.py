from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Labs, LabTopic

class LabsAdmin(SummernoteModelAdmin):
    exclude = ('lab_slug', )
    list_display = ('id', 'lab_title', 'lab_level', 'lab_date_created')
    list_display_links = ('id', 'lab_title')
    search_fields = ('lab_title', )
    list_per_page = 25
    summernote_fields = ('lab_content', 'lab_description')

class LabTopicAdmin(SummernoteModelAdmin):
    exclude = ('lab_topic_slug', )
    list_display = ('id', 'lab_topic_title', 'lab_topic_number', 'lab_topic_date_created')
    list_display_links = ('id', 'lab_topic_title')
    search_fields = ('lab_topic_title', )
    list_per_page = 25
    summernote_fields = ('lab_topic_content', 'lab_topic_description' )

admin.site.register(LabTopic, LabTopicAdmin)

admin.site.register(Labs, LabsAdmin)