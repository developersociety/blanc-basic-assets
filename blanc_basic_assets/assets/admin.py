from django.contrib import admin
from django.contrib.sites.models import Site
import urlparse
from .models import ImageCategory, Image, FileCategory, File


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class FileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Details', {
            'fields': ('category', 'title',)
        }),
        ('File', {
            'fields': ('file',)
        }),
    )

    list_display = ('title', 'category', 'file_location')
    list_filter = ('category',)
    search_fields = ('title',)

    def file_location(self, obj):
        domain = Site.objects.get_current().domain
        url = urlparse.urljoin('http://%s/' % domain, obj.get_absolute_url())
        return '<a href="%s">%s</a>' % (obj.get_absolute_url(), url)
    file_location.short_description = 'Location'
    file_location.allow_tags = True


admin.site.register((ImageCategory, FileCategory), CategoryAdmin)
admin.site.register((Image, File), FileAdmin)
