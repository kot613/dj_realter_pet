from django.contrib import admin

from .models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'city', 'price', 'realtor']
    list_display_links = ('id', 'title', 'realtor')
    search_fields = ('city', 'realtor')
