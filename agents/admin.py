from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Agent, MessageAgent


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    """ Register agents model for admin site"""
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['id', 'name', 'is_best', 'get_photo']
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    list_per_page = 10

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '<-_->'

    get_photo.short_description = 'Title'


@admin.register(MessageAgent)
class MessageAgentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'agent']
    list_display_links = ('id', 'name')
    list_per_page = 10
