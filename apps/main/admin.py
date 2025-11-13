from django.contrib import admin
from django.utils.html import format_html

from apps.main import models


class HistoryPhotoInline(admin.StackedInline):
    model = models.HistoryPhoto
    extra = 0
    max_num = 1


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.History)
class HistoryAdmin(admin.ModelAdmin):
    inlines = [HistoryPhotoInline]
    search_fields = ['name']
    list_filter = ['city', 'created_at']
    readonly_fields = ['created_at', 'updated_at']

    def photo_tag(self, obj):
        if hasattr(obj, 'photo') and obj.photo.photo:
            return format_html('<img src="{}" style="max-height:60px;"/>', obj.photo.photo.url)
        return "Нет фото"

    photo_tag.short_description = "Фото"
    list_display = ['id', 'name', 'photo_tag', 'city']


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'registration_type', 'created_at']
    search_fields = ['name']
    readonly_fields = ['created_at']
    list_filter = ['registration_type']


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'rating', 'created_at']
    search_fields = ['author']
    readonly_fields = ['created_at', 'updated_at']
    list_filter = ['rating', 'created_at']
