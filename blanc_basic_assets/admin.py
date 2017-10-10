from os.path import basename

from django.contrib import admin
from django.utils.html import format_html

from .models import File, FileCategory, Image, ImageCategory


@admin.register(ImageCategory, FileCategory)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)


@admin.register(Image, File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'file_link')
    list_filter = ('category',)
    search_fields = ('title',)

    def file_link(self, obj):
        return format_html(
            '<a href="{url}">{name}</a>', url=obj.get_absolute_url(), name=basename(obj.file.name)
        )
    file_link.short_description = 'Link'
