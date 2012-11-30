from django.db import models, transaction
from functools import update_wrapper
from django.contrib import admin
from django.contrib.admin import helpers
from django.contrib.admin.options import csrf_protect_m
from django.contrib.admin.widgets import AdminFileWidget
from django.contrib.sites.models import Site
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext
from django.utils.encoding import force_unicode
from .models import ImageCategory, Image, FileCategory, File
import urlparse
import os.path


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class FileAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.FileField: {'widget': AdminFileWidget(attrs={'multiple': ''})},
        models.ImageField: {'widget': AdminFileWidget(attrs={'multiple': ''})},
    }

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


    def get_urls(self):
        from django.conf.urls import patterns, url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.module_name

        urlpatterns = patterns('',
            url(r'^add-multiple/$',
                wrap(self.add_multiple_view),
                name='%s_%s_add_multiple' % info),
        )
        urlpatterns += super(FileAdmin, self).get_urls()
        return urlpatterns


    @csrf_protect_m
    @transaction.commit_on_success
    def add_multiple_view(self, request, form_url='', extra_context=None):
        "Replacement add view for multiple file upload."
        model = self.model
        opts = model._meta

        if not self.has_add_permission(request):
            raise PermissionDenied

        ModelForm = self.get_form(request)
        form = ModelForm()

        if request.method == 'POST':
            # 0 files uploaded, will error out
            if len(request.FILES.getlist('file')) == 0:
                form = ModelForm(request.POST, request.FILES)
                form.is_valid()

            # Multiple files
            else:
                # First wave - just validate all the files
                bad_upload = False

                for i in request.FILES.getlist('file'):
                    single_file = {'file': i}
                    form = ModelForm(request.POST, single_file)

                    # Invalid file, don't process any others
                    if not form.is_valid():
                        messages.warning(request, _('Failed to upload %(file)s' % {
                            'file': i.name,
                        }))
                        bad_upload = True

                # Inform the user that no files get saved if an error occurs
                if bad_upload:
                    messages.warning(request, _('No files have been saved'))

                # All files validated, now process again and save
                if not bad_upload:
                    success_count = 0

                    for i in request.FILES.getlist('file'):
                        single_file = {'file': i}
                        form = ModelForm(request.POST, single_file)

                        if form.is_valid():
                            new_object = form.save(commit=False)

                            # Add the file name to the title as well
                            file_name, file_ext = os.path.splitext(i.name)
                            title_prefix = new_object.title
                            title_suffix = u' - %s' % (file_name,)

                            # Shorten the existing title if needed
                            title_max_length = opts.get_field_by_name('title')[0].max_length - len(title_suffix)
                            if len(title_prefix) > title_max_length:
                                title_prefix = title_prefix[:title_max_length]

                            new_object.title = ''.join((title_prefix.strip(), title_suffix))

                            new_object.save()
                            self.log_addition(request, new_object)
                            success_count += 1

                        msg = ungettext(u'Successfully uploaded 1 file', u'Successfully uploaded %(count)d files', success_count)
                        messages.success(request, msg % {
                            'count': success_count,
                        })

                    # Redirect back if the user wants to
                    if '_addanother' in request.POST:
                        return HttpResponseRedirect(request.path)

                    # Figure out where to redirect. If the user has change permission,
                    # redirect to the change-list page for this object. Otherwise,
                    # redirect to the admin index.
                    if self.has_change_permission(request, None):
                        post_url = reverse('admin:%s_%s_changelist' %
                                           (opts.app_label, opts.module_name),
                                           current_app=self.admin_site.name)
                    else:
                        post_url = reverse('admin:index',
                                           current_app=self.admin_site.name)
                    return HttpResponseRedirect(post_url)
        else:
            # Prepare the dict of initial data from the request.
            # We have to special-case M2Ms as a list of comma-separated PKs.
            initial = dict(request.GET.items())
            for k in initial:
                try:
                    f = opts.get_field(k)
                except models.FieldDoesNotExist:
                    continue
                if isinstance(f, models.ManyToManyField):
                    initial[k] = initial[k].split(",")
            form = ModelForm(initial=initial)

        adminForm = helpers.AdminForm(form, list(self.get_fieldsets(request)),
            self.get_prepopulated_fields(request),
            self.get_readonly_fields(request),
            model_admin=self)
        media = self.media + adminForm.media

        context = {
            'add_multiple': True,
            'title': _('Add multiple %s') % force_unicode(opts.verbose_name_plural),
            'adminform': adminForm,
            'is_popup': False,
            'show_delete': False,
            'media': media,
            'errors': helpers.AdminErrorList(form, []),
            'app_label': opts.app_label,
        }
        context.update(extra_context or {})
        return self.render_change_form(request, context, form_url=form_url, add=True)


admin.site.register((ImageCategory, FileCategory), CategoryAdmin)
admin.site.register((Image, File), FileAdmin)
