from os.path import basename

from django.contrib import admin

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
        return '<a href="%s">%s</a>' % (obj.get_absolute_url(), basename(obj.file.name))
    file_link.short_description = 'Link'
    file_link.allow_tags = True
