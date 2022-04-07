from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import CTFFiles, CTFs, CTFsTopic

class CTFsAdmin(SummernoteModelAdmin):
    exclude = ('ctfs_slug', )
    list_display = ('id', 'ctfs_title', 'ctfs_level', 'ctfs_date_created')
    list_display_links = ('id', 'ctfs_title')
    search_fields = ('ctfs_title', )
    list_per_page = 25
    summernote_fields = ('ctfs_content', 'ctfs_topic_list')

class CTFsTopicAdmin(SummernoteModelAdmin):
    exclude = ('ctfs_topic_slug', )
    list_display = ('id', 'ctfs_topic_title', 'ctfs_topic_number', 'ctfs_topic_date_created')
    list_display_links = ('id', 'ctfs_topic_title')
    search_fields = ('ctfs_topic_title', )
    list_per_page = 25
    summernote_fields = ('ctfs_topic_content', )

class CTFsFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'ctffiledescription')
    list_display_links = ('id', 'ctffiledescription')
    search_fields = ('ctffiledescription', )
    list_per_page = 25

admin.site.register(CTFFiles, CTFsFilesAdmin)

admin.site.register(CTFs, CTFsAdmin)
admin.site.register(CTFsTopic, CTFsTopicAdmin)

