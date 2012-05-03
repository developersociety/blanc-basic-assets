from django.contrib import admin
from django.contrib.sites.models import Site
import urlparse
from .models import Image, File


class FileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Details', {
            'fields': ('title',)
        }),
        ('File', {
            'fields': ('file',)
        }),
    )

    list_display = ('title', 'file_location')

    def file_location(self, obj):
        domain = Site.objects.get_current().domain
        url = urlparse.urljoin('http://%s/' % domain, obj.get_absolute_url())
        return '<a href="%s">%s</a>' % (obj.get_absolute_url(), url)
    file_location.short_description = 'Location'
    file_location.allow_tags = True


admin.site.register((Image, File), FileAdmin)
