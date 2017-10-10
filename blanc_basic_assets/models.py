from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ImageCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'image categories'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Image(models.Model):
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    file = models.ImageField(
        'Image', upload_to='assets/image', height_field='image_height', width_field='image_width')
    image_height = models.PositiveIntegerField(editable=False)
    image_width = models.PositiveIntegerField(editable=False)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.file.url


@python_2_unicode_compatible
class FileCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'file categories'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class File(models.Model):
    category = models.ForeignKey(FileCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    file = models.FileField(upload_to='assets/file')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.file.url
