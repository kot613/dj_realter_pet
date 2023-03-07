from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Register comment model for admin site"""
    list_display = ['name', 'get_photo']
    list_display_links = ('name',)
    search_fields = ('name',)

    list_per_page = 10

    def get_photo(self, obj):
        """Adding small image in admin panel"""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '<-_->'

    get_photo.short_description = 'Image'
